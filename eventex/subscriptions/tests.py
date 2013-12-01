# coding: utf-8
from django.test import TestCase


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """
        GET /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.response.status_code)
