#!/usr/bin/env python3
"""Create clearly fictional supporting exhibits from the shared video fixture."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak


def build(output: Path, fixture: dict):
    styles = getSampleStyleSheet()
    story = []

    def section(title, paragraphs):
        if story:
            story.append(PageBreak())
        story.append(Paragraph(title, styles['Title']))
        story.append(Paragraph('FICTIONAL REHEARSAL EXHIBIT - NO CITY SUBMISSION', styles['Heading3']))
        for label, value in paragraphs:
            story.extend([Spacer(1, 12), Paragraph(escape(label), styles['Heading3']),
                          Paragraph(escape(value), styles['BodyText'])])

    assumptions = fixture['rehearsal_assumptions']
    section('E1 | Fictional property and scope', [
        ('Address label', fixture['address_disclaimer']),
        ('Provenance', assumptions['provenance']),
        ('Legal description', assumptions['legal_description']),
        ('Zoning', assumptions['zoning']),
        ('Site history', assumptions['site_history']),
        ('Constraint assumptions', assumptions['constraints']),
        ('Scope', fixture['fields']['description']),
    ])
    section('E2 | Equipment and conditional studies', [
        ('Equipment example', assumptions['equipment']),
        ('Noise and access', assumptions['noise_controls']),
        ('Water quality scenario', assumptions['water_quality']),
        ('Landscape', assumptions['landscape']),
        ('Lighting', assumptions['lighting']),
        ('Other study branches', assumptions['other_studies']),
    ])
    section('E3 | Simulated owner declaration', [
        ('Fictional owner', fixture['fields']['owner']),
        ('Purpose', 'This exhibit rehearses the owner-declaration step in physical page 33 of the official packet. It is not an affidavit, legal signature, authorization concerning City Hall, or agreement with the City.'),
        ('Scenario acknowledgment', 'Within this invented scenario, the named fictional owner has reviewed the fictional scope and documents. All property facts are authored assumptions; no actual ownership is represented.'),
        ('Simulated signature', fixture['fields']['owner'] + ' / DEMO ONLY / NOT LEGALLY EXECUTED'),
        ('Real filing distinction', 'The official affidavit requires a wet/scanned or authenticated electronic signature. A typed name alone is not accepted. This rehearsal exhibit does not satisfy that real requirement.'),
    ])
    section('E4 | Simulated applicant statements', [
        ('Fictional applicant', fixture['fields']['applicant']),
        ('Completeness acknowledgment', 'Rehearsal counterpart to physical page 41. The fictional applicant has seen the component register. No City completeness determination or legal execution is represented.'),
        ('Hazardous-site statement', 'Rehearsal counterpart to physical page 43. No actual hazardous-site search has been performed or certified for City Hall. The fictional branch assumes no listed site; replace with a sourced determination for a real project.'),
        ('Simulated signature', fixture['fields']['demo_signature'] + ' / DEMO ONLY / NOT LEGALLY EXECUTED'),
        ('Email update preference', assumptions['email_updates']),
        ('Review history', assumptions['prior_review']),
        ('Submission outcome', 'Only a local DEMO receipt may be created. No City approval, paid fee, permit or issuance is represented.'),
    ])

    def footer(c, doc):
        c.setFont('Helvetica', 8)
        c.drawString(42, 25, fixture['project_facts']['plan_revision'] + ' | FICTIONAL - NOT FOR CITY FILING')
        c.drawRightString(570, 25, str(doc.page))

    SimpleDocTemplate(str(output), leftMargin=42, rightMargin=42,
                      topMargin=40, bottomMargin=45).build(story, onFirstPage=footer, onLaterPages=footer)
