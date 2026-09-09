#!/usr/bin/env python3
"""Draw dimensioned fictional concept sheets from the shared demo fixture."""
import argparse
import json
from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
INK = HexColor('#173e35')
MUTED = HexColor('#566860')
BLUE = HexColor('#d6edf0')
PAPER = HexColor('#f7f6ef')


def text(c, x, y, value, size=10, font='Helvetica'):
    c.setFillColor(INK)
    c.setFont(font, size)
    c.drawString(x, y, str(value))


def lines(c, x, y, values, size=10, leading=16):
    for i, value in enumerate(values):
        text(c, x, y-i*leading, value, size)


def frame(c, sheet, title, fixture):
    c.setFillColor(PAPER); c.rect(0, 0, 792, 612, fill=1, stroke=0)
    c.setStrokeColor(INK); c.setLineWidth(.7); c.rect(24, 24, 744, 564, stroke=1, fill=0)
    text(c, 40, 563, 'CrossBeam', 24, 'Times-Roman')
    text(c, 215, 568, title, 16, 'Helvetica-Bold')
    text(c, 215, 548, 'FICTIONAL PROJECT - NOT FOR CONSTRUCTION OR CITY SUBMISSION', 9)
    c.line(24, 535, 768, 535); c.line(24, 58, 768, 58)
    text(c, 40, 39, '505 Forest Avenue is a demo label only. This drawing does not depict City Hall.', 9)
    text(c, 620, 39, fixture['project_facts']['plan_revision']+' | '+sheet, 10, 'Helvetica-Bold')


def dimension(c, start, end, label, vertical=False):
    c.setStrokeColor(MUTED); c.setLineWidth(.5)
    x1,y1=start; x2,y2=end
    c.line(x1,y1,x2,y2)
    if vertical:
        c.line(x1-4,y1,x1+4,y1); c.line(x2-4,y2,x2+4,y2)
        text(c,x1+6,(y1+y2)/2+6,label,8)
    else:
        c.line(x1,y1-4,x1,y1+4); c.line(x2,y2-4,x2,y2+4)
        c.setFont('Helvetica',8);c.setFillColor(INK);c.drawCentredString((x1+x2)/2,y1+6,label)


def draw(output, fixture):
    site=fixture['synthetic_site']; facts=fixture['project_facts']
    c=canvas.Canvas(str(output),pagesize=(792,612),invariant=1)
    c.setTitle('Fictional Laguna pool concept - '+facts['plan_revision'])
    frame(c,'A0','Project brief and drawing index',fixture)
    text(c,48,500,'A fictional pool project, ready to discuss.',22,'Times-Roman')
    lines(c,48,468,[
        'Scope: '+str(facts['pool_width_ft'])+' x '+str(facts['pool_length_ft'])+' foot residential swimming pool and equipment.',
        'Applicant: '+fixture['fields']['applicant'],
        'Owner: '+fixture['fields']['owner'],
        'Contact: '+fixture['fields']['email'],
        'Review history: no City or private review completed for this sample revision.',
    ])
    text(c,48,362,'DRAWING INDEX',11,'Helvetica-Bold')
    lines(c,48,339,['A0  Project brief, scope, and unresolved professional inputs',
                   'A1  Dimensioned fictional site layout',
                   'A2  Concept pool section and equipment layout'])
    text(c,48,264,'WHAT THESE DRAWINGS ESTABLISH',11,'Helvetica-Bold')
    lines(c,48,241,['The illustrated dimensions are authored demonstration assumptions from fixture.json.',
                   'They provide a consistent example for intake questions, document preparation, and uploads.',
                   'They are not measurements of 505 Forest Avenue or findings about its permit eligibility.'])
    text(c,48,170,'WHAT A REAL PROJECT STILL NEEDS',11,'Helvetica-Bold')
    lines(c,48,147,['Actual survey, zoning/coastal/bluff review, site constraints, and equipment specifications.',
                   'Applicable structural/geotechnical design, hydraulic/electrical design, and safety details.',
                   'Required professional review, declarations, and City-required attachments.',
                   'Type 114 intake is mapped; actual parcel eligibility is undetermined.'],size=10)
    c.showPage()

    frame(c,'A1','Fictional site layout',fixture)
    origin=(72,88); scale=3.5
    def point(x,y): return origin[0]+x*scale,origin[1]+y*scale
    def box(bounds, fill=None):
        x,y,w,h=bounds
        c.setStrokeColor(INK);c.setLineWidth(.8)
        if fill is not None:c.setFillColor(fill)
        c.rect(*point(x,y),w*scale,h*scale,stroke=1,fill=fill is not None)
    box([0,0,site['lot_width_ft'],site['lot_depth_ft']])
    box(site['house_bounds_ft'],HexColor('#e1e4db'))
    hx,hy,hw,hh=site['house_bounds_ft']
    lines(c,*point(hx+3,hy+hh/2),['FICTIONAL HOUSE',f'{hw} x {hh} ft'],size=9)
    px,py=site['pool_origin_ft'];pw=facts['pool_width_ft'];pl=facts['pool_length_ft']
    box([px,py,pw,pl],BLUE)
    lines(c,*point(px+1,py+pl/2+2),['POOL',f'{pw} x {pl}'],size=7,leading=10)
    box(site['equipment_bounds_ft'],HexColor('#e1e4db'))
    ex,ey,ew,eh=site['equipment_bounds_ft']
    c.line(*point(ex+ew,ey+eh/2),400,370);text(c,402,367,'Equipment',8)
    c.setDash(4,3);box(site['barrier_bounds_ft']);c.setDash()
    dimension(c,point(0,-5),point(site['lot_width_ft'],-5),f"{site['lot_width_ft']} ft lot")
    dimension(c,point(-5,0),point(-5,site['lot_depth_ft']),f"{site['lot_depth_ft']} ft",True)
    dimension(c,point(px+pw+3,py+pl),point(px+pw+3,site['lot_depth_ft']),f"{site['lot_depth_ft']-py-pl} ft",True)
    dimension(c,point(px,hy+hh),point(px,py),f'{py-hy-hh} ft',True)
    text(c,170,95,'FICTIONAL STREET FRONT',8)
    text(c,464,497,'LAYOUT ASSUMPTIONS',11,'Helvetica-Bold')
    lines(c,464,472,[f"Lot: {site['lot_width_ft']} x {site['lot_depth_ft']} ft",
        f'Pool water surface: {pw*pl} sq ft',f'Pool to rear line: {site["lot_depth_ft"]-py-pl} ft',
        f'Pool to left line: {px} ft',f'Pool to right line: {site["lot_width_ft"]-px-pw} ft',
        f'Pool to house: {py-hy-hh} ft',f'Equipment pad: {ew} x {eh} ft'],size=10,leading=22)
    text(c,464,292,'READ THIS AS A CONCEPT',11,'Helvetica-Bold')
    lines(c,464,268,['Dashed enclosure: barrier concept only.',
        'Gate location and hardware unresolved.',
        'Dimensions are not approved setbacks.',
        'No real boundaries or easements shown.',
        'Equipment noise and siting unverified.',
        'Orientation is diagrammatic.'],size=9,leading=20)
    text(c,464,114,'Scale: 3.5 printed points per fictional foot.',9)
    text(c,464,96,'Use dimensions; do not scale a video image.',9)
    c.showPage()

    frame(c,'A2','Pool section and equipment concept',fixture)
    text(c,48,502,'LONGITUDINAL SECTION - CONCEPT ONLY',11,'Helvetica-Bold')
    x,y,section_scale=72,422,15
    length=facts['pool_length_ft']; shallow=site['shallow_depth_ft'];deep=site['deep_depth_ft']
    path=c.beginPath();path.moveTo(x,y);path.lineTo(x+length*section_scale,y)
    path.lineTo(x+length*section_scale,y-deep*section_scale)
    path.lineTo(x+6*section_scale,y-shallow*section_scale)
    path.lineTo(x,y-shallow*section_scale);path.close()
    c.setFillColor(BLUE);c.setStrokeColor(INK);c.drawPath(path,fill=1,stroke=1)
    dimension(c,(x,y+20),(x+length*section_scale,y+20),f'{length} ft water length')
    dimension(c,(x-15,y-shallow*section_scale),(x-15,y),f'{shallow} ft',True)
    dimension(c,(x+length*section_scale+15,y-deep*section_scale),(x+length*section_scale+15,y),f'{deep} ft',True)
    lines(c,540,453,['All section dimensions are fictional.',
        'Shell thickness / reinforcing: unresolved.',
        'Coping / grade relationship: unresolved.',
        'Drains / suction outlets: unresolved.',
        'No engineering or safety approval.'],size=9,leading=20)
    text(c,48,285,'EQUIPMENT PAD - DIAGRAMMATIC',11,'Helvetica-Bold')
    ew,eh=site['equipment_bounds_ft'][2:]
    c.setStrokeColor(INK);c.setFillColor(HexColor('#e1e4db'));c.rect(72,142,ew*36,eh*24,stroke=1,fill=1)
    text(c,90,207,'Pump / filter / controls',12)
    text(c,90,184,'Locations to be designed',10)
    dimension(c,(72,125),(72+ew*36,125),f'{ew} ft pad')
    lines(c,365,245,[f'Pad assumption: {ew} x {eh} ft.',
        'No equipment models, flow rates, or power loads selected.',
        'Pipe sizing, electrical bonding, and protection require design.',
        'Barrier, gate, alarm, and other applicable safety details remain open.',
        'Use this sheet to ask for missing inputs, not to assert compliance.'],size=10,leading=23)
    c.showPage();c.save()


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    draw(args.output,json.loads((ROOT/'fixture.json').read_text()))
