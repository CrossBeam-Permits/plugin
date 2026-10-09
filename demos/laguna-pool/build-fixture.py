#!/usr/bin/env python3
"""Generate explicitly synthetic rehearsal files; neither is an official application."""
import argparse
import hashlib
import json
import runpy
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent


def build(output):
    fixture = json.loads((ROOT / 'fixture.json').read_text())
    output.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    story = [Paragraph('CrossBeam | Fictional pool project', styles['Title']), Spacer(1, 18),
             Paragraph(fixture['label'], styles['Heading2']),
             Paragraph('SAMPLE INTAKE SUMMARY - NOT AN OFFICIAL CITY APPLICATION', styles['Heading3']),
             Paragraph(fixture['address_disclaimer'], styles['BodyText'])]
    for key, value in fixture['fields'].items():
        story += [Spacer(1, 12), Paragraph(escape(key.replace('_', ' ').title()), styles['Heading3']),
                  Paragraph(escape(value), styles['BodyText'])]
    story += [Spacer(1, 18), Paragraph('Type 114 intake is mapped; actual parcel eligibility remains undetermined. Real parcel, coastal, bluff, setback, and approval facts are unknown. The fictional signature is simulated; no payment is included.', styles['BodyText'])]
    SimpleDocTemplate(str(output / 'sample-application.pdf')).build(story)
    runpy.run_path(str(ROOT / 'build-exhibits.py'))['build'](output / 'fictional-exhibits.pdf', fixture)
    sample = PdfWriter()
    sample.append(PdfReader(output / 'sample-application.pdf'))
    sample.append(PdfReader(output / 'fictional-exhibits.pdf'))
    with (output / 'sample-application.pdf').open('wb') as stream:
        sample.write(stream)
    draw_plans = runpy.run_path(str(ROOT / 'draw-plans.py'))['draw']
    draw_plans(output / 'sample-plans.pdf', fixture)
    (output / 'drawing-register.md').write_text(
        '# Fictional drawing register\n\n'
        'Source: fixture.json synthetic_site and project_facts. Author: CrossBeam demo generator.\n'
        'No professional review or City approval. All sheets are fictional concepts only.\n\n'
        '| Sheet | Title | Revision | Status |\n|---|---|---|---|\n'
        + ''.join(f"| {sheet} | {title} | {fixture['project_facts']['plan_revision']} | Fictional concept |\n"
                  for sheet, title in [('A0', 'Project brief'), ('A1', 'Site layout'), ('A2', 'Pool section and equipment'), ('A3', 'Fictional survey'), ('A4', 'Perpendicular site sections'), ('A5', 'Grading and summary')])
        + '\nMissing: real survey/constraints, structural/geotechnical design, hydraulic/electrical design, '
        'equipment specifications, barrier/safety details, and complete supporting materials required by the applicable City forms.\n'
    )
    components = json.loads((ROOT / 'packet-components.json').read_text())
    (output / 'packet-components.json').write_text(json.dumps(components, indent=2)+'\n')
    manifest = {'fixture':fixture, 'files':{}, 'component_register':'packet-components.json'}
    for category, filename in [('Application','sample-application.pdf'),('Plans','sample-plans.pdf')]:
        raw = (output / filename).read_bytes()
        manifest['files'][category] = dict(name=filename, size=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    (output / 'fixture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    build(parser.parse_args().output_dir)
