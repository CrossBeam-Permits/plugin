#!/usr/bin/env python3
"""Use an installed plugin's helpers to prepare a labeled official-form demo copy."""
import argparse
import hashlib
import io
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin-dir', type=Path, required=True)
    parser.add_argument('--source-pdf', type=Path, required=True, help='Freshly acquired official Zone Clearance PDF')
    parser.add_argument('--packet-dir', type=Path, required=True, help='Directory created by build-fixture.py')
    args = parser.parse_args()
    plugin, output = args.plugin_dir.resolve(), args.packet_dir.resolve()
    manifest_path = output / 'fixture-manifest.json'
    packet = json.loads(manifest_path.read_text())
    fixture = json.loads((ROOT / 'fixture.json').read_text())
    if packet['fixture']['fields'] != fixture['fields']:
        raise ValueError('Rebuild the sample packet after changing fixture inputs')
    packet['fixture'] = fixture
    forms = json.loads((plugin/'assets/form-manifest.json').read_text())['forms']
    source = next(f for f in forms if f['id'] == 'zone-clearance-application')
    if hashlib.sha256(args.source_pdf.read_bytes()).hexdigest() != source['sha256']:
        raise ValueError('Official source hash differs from the installed plugin; refresh/remap first')
    maps = json.loads((plugin/'assets/field-maps/zone-clearance-application.json').read_text())['canonical_mappings']
    fields = fixture['fields']
    values = {**fixture['official_form_facts'], 'site.address':fields['address'], 'applicant.contact_name':fields['applicant'],
              'applicant.phone':fixture['contacts']['applicant_phone'], 'applicant.email':fields['email'],
              'owner.contact_name':fields['owner'], 'project.description':fields['description']}
    now = datetime.now(timezone.utc).isoformat()
    facts = []
    for mapping in maps:
        key = mapping['fact_id']
        if key not in values:
            continue
        controlled = mapping['applicant_controlled']
        facts.append({'id':key, 'value':values[key],
          'source':{'kind':'user_confirmed' if controlled else 'plan', 'receipt':{
            'kind':'user_answer' if controlled else 'file', 'captured_at':now, 'file':'fixture.json',
            'page':None,'sheet':fixture['project_facts']['plan_revision'],'field':key,'record_id':None,
            'note':'Synthetic fixture authorization only; not a real applicant declaration. Phone is a reserved fictional example.'}},
          'confidence':1, 'confirmation':{'required':controlled,'status':'confirmed' if controlled else 'not_required',
            'confirmed_at':now if controlled else None,'note':'Fictional demonstration only'},
          'consumers':[],'conflicts':[],'notes':['Not for City submission']})
    facts_path = output/'official-demo-facts.json'
    facts_path.write_text(json.dumps({'schema_version':'1.0.0','run_id':fixture['fixture_id'],
        'jurisdiction':'laguna-beach-ca','created_at':now,'updated_at':now,'facts':facts},indent=2)+'\n')
    def run(script, *params):
        subprocess.run([sys.executable,str(plugin/'scripts'/script),*map(str,params)],check=True)
    run('validate-json.py','--schema',plugin/'schemas/project-facts.schema.json',facts_path)
    working = output/'zone-clearance-working.pdf'
    run('fill-form.py','--input',args.source_pdf,'--facts',facts_path,'--field-map',
        plugin/'assets/field-maps/zone-clearance-application.json','--output',working)
    # Preserve the complete interactive City form and mark every page as a demonstration.
    writer = PdfWriter()
    writer.clone_document_from_reader(PdfReader(working))
    for page in writer.pages:
        width,height = float(page.mediabox.width),float(page.mediabox.height)
        stream=io.BytesIO(); stamp=canvas.Canvas(stream,pagesize=(width,height))
        stamp.setFillColorRGB(1,1,1);stamp.rect(0,height-18,width,18,stroke=0,fill=1)
        stamp.setFillColorRGB(.09,.24,.20);stamp.setFont('Helvetica-Bold',8)
        stamp.drawCentredString(width/2,height-12,'DEMONSTRATION - FICTIONAL INPUTS - NOT A CITY SUBMISSION')
        stamp.save();stream.seek(0);page.merge_page(PdfReader(stream).pages[0])
    final=output/'zone-clearance-demo.pdf'
    with final.open('wb') as stream: writer.write(stream)
    answers=output/'zone-clearance-working.answers-used.json'
    run('verify-form.py','--pdf',final,'--answers',answers)
    raw=final.read_bytes()
    packet['files']['Application']={'name':final.name,'size':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    packet['official_form']={'id':source['id'],'source_sha256':source['sha256'],
        'mapped_answers_filled':len(json.loads(answers.read_text())['answers']),
        'unmapped_and_unknown_fields':'remaining exhibits and non-widget declarations require separate completion; not a filing-ready project packet',
        'all_pages_labeled':len(writer.pages),'visual_review':'required'}
    manifest_path.write_text(json.dumps(packet,indent=2)+'\n')
    print(json.dumps(packet['official_form']))


if __name__ == '__main__':
    main()
