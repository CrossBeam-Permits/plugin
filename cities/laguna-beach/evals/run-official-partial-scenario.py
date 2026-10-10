#!/usr/bin/env python3
"""Verify missing and null facts leave actual City PDF fields blank, including CONFORMS."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--forms-dir', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    output = Path(args.output_dir).resolve()
    subprocess.run([sys.executable, str(ROOT / 'evals/run-official-pool-scenario.py'),
                    '--forms-dir', args.forms_dir, '--output-dir', str(output / 'full')], check=True)
    facts = json.loads((output / 'full/project-facts.json').read_text())
    mappings = json.loads((ROOT / 'assets/field-maps/design-review-application.json').read_text())['canonical_mappings']
    conformance_ids = {m['fact_id'] for m in mappings if m['transform'] == 'yes_no'}
    withheld = {f['id'] for i, f in enumerate(facts['facts']) if i % 2 == 0} | conformance_ids
    partial = []
    for i, fact in enumerate(facts['facts']):
        if fact['id'] in withheld:
            if i % 2 == 0:
                continue  # absent fact
            fact['value'] = None  # explicitly unknown fact
        partial.append(fact)
    facts['facts'] = partial
    facts_path = output / 'partial-facts.json'
    facts_path.write_text(json.dumps(facts, indent=2) + '\n')
    pdf = output / 'partial.pdf'
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/fill-form.py'),
                            '--input', str(Path(args.forms_dir) / 'design-review-application.pdf'),
                            '--facts', str(facts_path), '--field-map', str(ROOT / 'assets/field-maps/design-review-application.json'),
                            '--output', str(pdf), '--allow-partial'])
    assert result.returncode == 2, 'Missing required facts must remain blocked'
    full_answers = json.loads((output / 'full/design-review-pool-filled.answers-used.json').read_text())['answers']
    partial_answers = json.loads((output / 'partial.answers-used.json').read_text())['answers']
    assert {a['fact_id'] for a in partial_answers}.isdisjoint(withheld)
    assert len(partial_answers) == sum(a['fact_id'] not in withheld for a in full_answers)
    fields = PdfReader(pdf).get_fields()
    blank_names = {a['pdf_field'] for a in full_answers if a['fact_id'] in withheld}
    for name in blank_names:
        assert str(fields[name].get('/V', '')) == '', (name, fields[name].get('/V'))
    # Logical widget values are checked here; rendered appearance review follows.
    sys.path.insert(0, str(ROOT / 'scripts'))
    from _lib import full_field_name
    for page in PdfReader(pdf).pages:
        for reference in page.get('/Annots') or []:
            widget = reference.get_object()
            name = full_field_name(widget)
            if name in blank_names:
                assert str(widget.get('/V', '')) == '', name
    subprocess.run([sys.executable, str(ROOT / 'scripts/verify-form.py'), '--pdf', str(pdf),
                    '--answers', str(output / 'partial.answers-used.json')], check=True)
    for page in (2, 25):
        subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-png', '-r', '110',
                        '-singlefile', str(pdf), str(output / f'page-{page}')], check=True, capture_output=True)
    report = {'not_for_submission': True, 'filled_targets': len(partial_answers),
              'withheld_targets_verified_blank': len(blank_names),
              'conformance_facts_withheld': len(conformance_ids), 'visual_review': 'required'}
    (output / 'partial-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
