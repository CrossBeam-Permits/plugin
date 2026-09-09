import base64
import json
from pathlib import Path
import tempfile
import unittest
import server


class DemoTransactions(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'demo.sqlite3'
        self.db = server.connect(self.path)
        self.case = dict(id='DEMO-TEST', label=server.LABEL, status='saved_draft',
                         fields={key: None for key in server.FIELDS}, attachments={}, receipt=None)
        server.save_case(self.db, self.case)
        self.db.commit()

    def tearDown(self):
        self.db.close()
        self.temp.cleanup()

    def command(self, action, **data):
        with self.db:
            return server.mutate(self.db, self.case['id'], action, data)

    def fill(self):
        self.command('save', fields={**{key: 'Fictional demonstration' for key in server.FIELDS}, 'square_footage': '288'})
        for category in server.CATEGORIES:
            self.command('upload', category=category, name='sample.pdf',
                         base64=base64.b64encode(b'%PDF-1.4\nDEMONSTRATION').decode())

    def test_missing_inputs_block_without_inventing_them(self):
        self.command('save', fields={'address': '505 Forest Avenue — DEMO'})
        with self.assertRaisesRegex(ValueError, 'prior_review.*Application.*Plans'):
            self.command('submit')
        self.assertIsNone(server.read_case(self.db, self.case['id'])['fields']['prior_review'])
        self.assertEqual(server.read_case(self.db, self.case['id'])['status'], 'saved_draft')

    def test_missing_attachment_blocks_even_with_all_fields(self):
        self.command('save', fields={**{key: 'Synthetic' for key in server.FIELDS}, 'square_footage': '288'})
        with self.assertRaisesRegex(ValueError, 'Application, Plans'):
            self.command('submit')

    def test_signature_and_area_are_required_before_submission(self):
        self.fill()
        fields = server.read_case(self.db, self.case['id'])['fields']
        for key in ('demo_signature', 'square_footage'):
            self.command('save', fields={**fields, key: None})
            with self.assertRaisesRegex(ValueError, key):
                self.command('submit')
        for value in ('NaN', 'Infinity', '-1', '0', 'not an area'):
            with self.assertRaisesRegex(ValueError, 'positive finite'):
                self.command('save', fields={**fields, 'square_footage': value})
        self.command('save', fields=fields)
        self.assertTrue(self.command('submit')['receipt']['signature_is_simulated'])

    def test_receipt_survives_restart_and_submit_retry(self):
        self.fill()
        first = self.command('submit')
        self.db.close()
        self.db = server.connect(self.path)
        self.assertEqual(first, self.command('submit'))
        self.assertFalse(first['receipt']['city_submission'])
        self.assertTrue(first['receipt']['record_number'].startswith('DEMO-'))
        self.assertEqual(self.db.execute('SELECT count(*) FROM cases').fetchone()[0], 1)
        with self.assertRaisesRegex(ValueError, 'cannot be changed'):
            self.command('save', fields={})

    def test_upload_integrity_and_no_file_bytes_in_receipt(self):
        self.fill()
        public = self.command('submit')
        stored = server.read_case(self.db, self.case['id'])
        for category in server.CATEGORIES:
            item = stored['attachments'][category]
            self.assertEqual(server.hashlib.sha256(base64.b64decode(item['base64'])).hexdigest(), item['sha256'])
            self.assertNotIn('base64', public['attachments'][category])

    def test_reject_bad_files_categories_and_field_types(self):
        for data in [dict(category='Wrong', name='x.pdf', base64=''),
                     dict(category='Plans', name='x.pdf', base64=base64.b64encode(b'not pdf').decode()),
                     dict(category='Plans', name='x.exe', base64=''),
                     dict(category='Plans', name='x.pdf', base64='???')]:
            with self.assertRaises(ValueError):
                self.command('upload', **data)
        with self.assertRaises(ValueError):
            self.command('save', fields={'address': {'injected': 'object'}})
        self.assertEqual(server.read_case(self.db, self.case['id'])['attachments'], {})


class DemoHTTP(unittest.TestCase):
    def test_http_mutations_persist_and_cross_origin_is_rejected(self):
        import threading
        import urllib.request
        import urllib.error
        with tempfile.TemporaryDirectory() as directory:
            http = server.HTTPServer(('127.0.0.1', 0), server.Handler)
            http.db_path = Path(directory) / 'state.sqlite3'
            worker = threading.Thread(target=http.serve_forever, daemon=True)
            worker.start()
            url = f'http://127.0.0.1:{http.server_port}'
            def request(path, data=None, origin=None):
                headers = {'Content-Type':'application/json'}
                if origin:
                    headers['Origin'] = origin
                body = None if data is None else json.dumps(data).encode()
                with urllib.request.urlopen(urllib.request.Request(url+path, data=body, headers=headers)) as response:
                    return json.load(response)
            try:
                case = request('/api/cases', {})
                request('/api/cases/'+case['id']+'/save', {'fields':{'address':'505 Forest Avenue (DEMO ONLY)'}})
                self.assertEqual(request('/api/cases/'+case['id'])['fields']['address'], '505 Forest Avenue (DEMO ONLY)')
                with self.assertRaises(urllib.error.HTTPError) as caught:
                    request('/api/cases', {}, 'https://unrelated.example')
                self.assertEqual(caught.exception.code, 403)
                caught.exception.close()
            finally:
                http.shutdown()
                worker.join()
                http.server_close()

    def test_accepts_official_form_size_but_bounds_local_uploads(self):
        content = b'%PDF-' + b'0' * (9 * 1024 * 1024)
        result = server.attachment({'name':'official-demo.pdf','base64':base64.b64encode(content).decode()})
        self.assertEqual(result['size'],len(content))
        with self.assertRaisesRegex(ValueError, '16 MB'):
            server.attachment({'name':'too-large.pdf','base64':base64.b64encode(content*2).decode()})


if __name__ == '__main__':
    unittest.main()
