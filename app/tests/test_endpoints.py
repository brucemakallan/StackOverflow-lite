import unittest

from flask import json

from app.views import app


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.test_data_question = dict(
            question='What is a variable'
        )
        self.test_data_answer = {
            "date_posted": "Fri, 03 Aug 2018 00:00:00 GMT",
            "answer": "A storage construct whose value can change",
            "id": 1,
            "question_id": 1,
            "votes": 12
        }

    # test for endpoints. Run using $pytest
    def test_get_all_questions(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client.get('/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_question(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_one_question(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client.get('/api/v1/questions/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_answer(self):
        res = self.client.post('/api/v1/questions/1/answers', data=json.dumps(self.test_data_answer), content_type='application/json')
        self.assertEqual(res.status_code, 201)
