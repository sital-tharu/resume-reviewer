from flask import Flask, jsonify
import os
import unittest

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_upload_resume(self):
        with self.client:
            response = self.client.post('/upload', data={
                'resume': (open('tests/test_resume.pdf', 'rb'), 'test_resume.pdf')
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Upload successful', response.data)

    def test_get_feedback(self):
        response = self.client.get('/feedback/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AI Feedback', response.data)

if __name__ == '__main__':
    unittest.main()