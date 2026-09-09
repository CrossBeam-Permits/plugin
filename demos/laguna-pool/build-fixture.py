#!/usr/bin/env python3
"""Generate explicitly synthetic rehearsal files; neither is an official application."""
import argparse
import hashlib
import json
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
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
    story += [Spacer(1, 18), Paragraph('Route and eligibility remain unverified. Real parcel, coastal, bluff, setback, and approval facts are unknown. No signature or payment is included.', styles['BodyText'])]
    SimpleDocTemplate(str(output / 'sample-application.pdf')).build(story)
    story = [Paragraph('CrossBeam | Sample plan inputs', styles['Title']), Spacer(1, 18),
             Paragraph(fixture['label'], styles['Heading2']),
             Paragraph('DEMO-R1 - PLACEHOLDER FOR BROWSER UPLOAD TESTING', styles['Heading3']),
             Paragraph('This is not a construction plan, survey, engineering design, or permit-ready plan sheet.', styles['BodyText']), Spacer(1, 18)]
    facts = fixture['project_facts']
    table = Table([['Fictional input', 'Value'], ['Pool width', f"{facts['pool_width_ft']} feet"], ['Pool length', f"{facts['pool_length_ft']} feet"], ['Water surface area', f"{facts['pool_area_sq_ft']} square feet"], ['Plan revision', facts['plan_revision']], ['City review', 'Not completed']], colWidths=[240, 220])
    table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#173e35')), ('TEXTCOLOR',(0,0),(-1,0),colors.white), ('BOTTOMPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),12),('GRID',(0,0),(-1,-1),0.4,colors.lightgrey)]))
    story += [table, Spacer(1, 24), Paragraph(fixture['address_disclaimer'], styles['BodyText']), Spacer(1, 18), Paragraph('No real APN, zoning, coastal status, bluff status, setbacks, equipment siting, structural details, or safety compliance is asserted. These unknowns prevent a production filing; this file exists only to exercise a fictional upload.', styles['BodyText'])]
    SimpleDocTemplate(str(output / 'sample-plans.pdf')).build(story)
    manifest = {'fixture':fixture, 'files':{}}
    for category, filename in [('Application','sample-application.pdf'),('Plans','sample-plans.pdf')]:
        raw = (output / filename).read_bytes()
        manifest['files'][category] = dict(name=filename, size=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    (output / 'fixture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    build(parser.parse_args().output_dir)
