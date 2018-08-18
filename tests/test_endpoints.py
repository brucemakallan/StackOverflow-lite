import unittest

from flask import app


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.test_data_question = {
            "date_posted": "Wed, 01 Aug 2018 00:00:00 GMT",
            "details": "What is a variable?",
            "id": 1
        }
        self.test_data_answer = {
            "date_posted": "Fri, 03 Aug 2018 00:00:00 GMT",
            "details": "A storage construct whose value can change",
            "id": 1,
            "question_id": 1,
            "votes": 12
        }

    # test for endpoints. Run using $pytest
    def test_get_all_questions(self):
        res = self.client.post('/api/v1/questions', data=self.test_data_question)
        self.assertEqual(res.status_code, 201)
        response = self.client.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)

    def test_post_question(self):
        res = self.client.post('/api/v1/questions', data=self.test_data_question)
        self.assertEqual(res.status_code, 201)

    def test_get_one_question(self):
        res = self.client.post('/api/v1/questions', data=self.test_data_question)
        self.assertEqual(res.status_code, 201)
        response = self.client.get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)

    def test_post_answer(self):
        res = self.client.post('/api/v1/questions/1/answers', data=self.test_data_answer)
        self.assertEqual(res.status_code, 201)
