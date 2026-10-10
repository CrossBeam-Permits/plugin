#!/usr/bin/env python3
"""Compare a browser-created demo receipt and persisted uploads to the fixture."""
import argparse
import base64
import hashlib
import json
import sqlite3
from pathlib import Path


def verify(db_path, case_id, manifest_path):
    manifest = json.loads(manifest_path.read_text())
    with sqlite3.connect(db_path) as db:
        row = db.execute('SELECT body FROM cases WHERE id=?', (case_id,)).fetchone()
        if row is None:
            raise ValueError('Browser-created case not found')
        case = json.loads(row[0])
    if case['fields'] != manifest['fixture']['fields']:
        raise ValueError('Submitted values differ from the fictional fixture')
    if case['status'] != 'demo_submitted' or case['receipt']['city_submission'] is not False:
        raise ValueError('Expected a completed simulation, never a City submission')
    if case['receipt']['record_number'] != case_id or not case_id.startswith('DEMO-'):
        raise ValueError('Receipt identity is inconsistent')
    if set(case['attachments']) != set(manifest['files']):
        raise ValueError('Attachment categories differ from the fixture')
    for category, expected in manifest['files'].items():
        actual = case['attachments'][category]
        raw = base64.b64decode(actual['base64'], validate=True)
        observed = dict(name=actual['name'], size=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if observed != expected or observed['sha256'] != actual['sha256']:
            raise ValueError(f'{category} uploaded bytes differ from the fixture')
    return dict(case_id=case_id, city_submission=False, fields_compared=len(case['fields']),
                files_compared=len(case['attachments']), receipt=case['receipt'],
                uploaded_files=manifest['files'], result='pass')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--case-id', required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.database, args.case_id, args.manifest)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
