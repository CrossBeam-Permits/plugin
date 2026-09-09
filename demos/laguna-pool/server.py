#!/usr/bin/env python3
"""Loopback-only fictional permit rehearsal. No City connections or credentials."""
import argparse
import base64
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from contextlib import closing
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

ROOT = Path(__file__).resolve().parent
LABEL = 'DEMONSTRATION — NOT A CITY SUBMISSION'
FIELDS = ('address', 'description', 'applicant', 'owner', 'email', 'prior_review')
CATEGORIES = ('Application', 'Plans')
LIMIT = 24 * 1024 * 1024


def connect(path):
    db = sqlite3.connect(path)
    db.execute('CREATE TABLE IF NOT EXISTS cases (id TEXT PRIMARY KEY, body TEXT NOT NULL)')
    return db


def read_case(db, case_id):
    row = db.execute('SELECT body FROM cases WHERE id = ?', (case_id,)).fetchone()
    if row is None:
        raise LookupError('Demo case not found')
    return json.loads(row[0])


def save_case(db, case):
    db.execute('INSERT OR REPLACE INTO cases VALUES (?, ?)', (case['id'], json.dumps(case)))


def public_case(case):
    return {**case, 'attachments': {
        category: {key: value for key, value in item.items() if key != 'base64'}
        for category, item in case['attachments'].items()
    }}


def validate_fields(fields):
    if not isinstance(fields, dict) or set(fields) - set(FIELDS):
        raise ValueError('Unexpected project fields')
    if any(not isinstance(v, (str, type(None))) or len(v or '') > 5000 for v in fields.values()):
        raise ValueError('Project values must be text or unknown (null)')
    return {k: (fields.get(k) or '').strip() or None for k in FIELDS}


def attachment(data):
    name = data.get('name')
    if not isinstance(name, str) or not name.lower().endswith('.pdf') or len(name) > 200:
        raise ValueError('Choose a PDF with a filename of at most 200 characters')
    try:
        raw = base64.b64decode(data.get('base64', ''), validate=True)
    except (ValueError, TypeError) as exc:
        raise ValueError('Invalid file encoding') from exc
    if not raw.startswith(b'%PDF-') or len(raw) > 16 * 1024 * 1024:
        raise ValueError('Choose a PDF of at most 16 MB')
    return dict(name=Path(name).name, size=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
                base64=base64.b64encode(raw).decode())


def missing(case):
    result = [k for k in FIELDS if not case['fields'].get(k)]
    result += [k for k in CATEGORIES if k not in case['attachments']]
    return result


def mutate(db, case_id, action, data):
    case = read_case(db, case_id)
    if case['status'] == 'demo_submitted':
        if action == 'submit':
            return public_case(case)  # A retry returns the original immutable receipt.
        raise ValueError('Submitted demo cases cannot be changed')
    if action == 'save':
        case['fields'] = validate_fields(data.get('fields'))
    elif action == 'upload':
        category = data.get('category')
        if category not in CATEGORIES:
            raise ValueError('Unknown attachment category')
        case['attachments'][category] = attachment(data)
    elif action == 'submit':
        gaps = missing(case)
        if gaps:
            raise ValueError('Missing required demo inputs: ' + ', '.join(gaps))
        case['status'] = 'demo_submitted'
        case['receipt'] = {
            'record_number': case['id'], 'label': LABEL,
            'submitted_at': datetime.now(timezone.utc).isoformat(),
            'city_submission': False, 'payment': 'No payment — simulation',
            'next_step': 'Demo complete. No City review, approval, or permit was requested.',
            'mapping_status': 'Zone Clearance production entry remains unverified',
        }
    else:
        raise LookupError('Unknown action')
    save_case(db, case)
    return public_case(case)


class Handler(BaseHTTPRequestHandler):
    def reply(self, status, body, content_type='application/json'):
        raw = json.dumps(body).encode() if content_type == 'application/json' else body
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(raw)

    def local_request(self):
        origin = 'http://' + self.headers.get('Host', '')
        allowed = (f'http://127.0.0.1:{self.server.server_port}', f'http://localhost:{self.server.server_port}')
        return origin in allowed and self.headers.get('Origin', origin) == origin

    def do_GET(self):
        if not self.local_request():
            return self.reply(403, {'error': 'Local requests only'})
        path = urlparse(self.path).path
        assets = {'/': ('index.html', 'text/html; charset=utf-8'),
                  '/app.js': ('app.js', 'text/javascript'), '/style.css': ('style.css', 'text/css')}
        if path in assets:
            filename, mime = assets[path]
            return self.reply(200, (ROOT / filename).read_bytes(), mime)
        if path.startswith('/api/cases/'):
            try:
                with closing(connect(self.server.db_path)) as db:
                    case = read_case(db, path.removeprefix('/api/cases/'))
                return self.reply(200, public_case(case))
            except LookupError as exc:
                return self.reply(404, {'error': str(exc)})
        return self.reply(404, {'error': 'Not found'})

    def do_POST(self):
        if not self.local_request() or self.headers.get('Content-Type') != 'application/json':
            return self.reply(403, {'error': 'Same-origin JSON requests only'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= LIMIT:
                raise ValueError('Request is empty or too large')
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError('Expected a JSON object')
            path = urlparse(self.path).path
            with closing(connect(self.server.db_path)) as db, db:
                db.execute('BEGIN IMMEDIATE')
                if path == '/api/cases':
                    case = dict(id='DEMO-' + uuid4().hex[:12].upper(), label=LABEL,
                                status='saved_draft', fields={k: None for k in FIELDS}, attachments={}, receipt=None)
                    save_case(db, case)
                    result = public_case(case)
                else:
                    parts = path.strip('/').split('/')
                    if len(parts) != 4 or parts[:2] != ['api', 'cases']:
                        raise LookupError('Unknown action')
                    result = mutate(db, parts[2], parts[3], data)
            self.reply(200, result)
        except (ValueError, TypeError) as exc:
            self.reply(400, {'error': str(exc)})
        except LookupError as exc:
            self.reply(404, {'error': str(exc)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir', type=Path, required=True, help='Private output directory for the demo database')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    args.state_dir.mkdir(parents=True, exist_ok=True)
    server = HTTPServer(('127.0.0.1', args.port), Handler)
    server.db_path = args.state_dir / 'demo.sqlite3'
    with closing(connect(server.db_path)):
        pass
    print(f'{LABEL}\nhttp://127.0.0.1:{server.server_port}', flush=True)
    server.serve_forever()


if __name__ == '__main__':
    main()
