import unittest

from flask import json

from app.views import app


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.test_data_question1 = dict(question='Test question 1')
        self.test_data_question2 = dict(question='Test question 2')
        self.test_data_question3 = dict(question='Test question 3')
        self.test_data_answer = {
            "date_posted": "Fri, 03 Aug 2018 00:00:00 GMT",
            "answer": "Test answer 1",
            "id": 1,
            "question_id": 1
        }

    # test for endpoints. Run using $pytest
    def test_get_all_questions(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question1), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client.get('/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_question(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question2), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    # test if same question is posted
    def test_post_duplicate_question(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question1), content_type='application/json')
        self.assertEqual(res.status_code, 409)  # 409 Conflict (Due to duplicate value)

    def test_get_one_question(self):
        res = self.client.post('/api/v1/questions', data=json.dumps(self.test_data_question3), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client.get('/api/v1/questions/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_answer(self):
        res = self.client.post('/api/v1/questions/1/answers', data=json.dumps(self.test_data_answer), content_type='application/json')
        self.assertEqual(res.status_code, 201)
