# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='Matheus Guilarducci',
            cpf='01234567890',
            email='email@example.com',
            phone='21-99999-8888'
        )
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        """
        GET /inscricao/1/ must return status code 200
        """
        self.assertTrue(200, self.resp.status_code)

    def test_template(self):
        """
        Uses template
        """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        """
        Context must have a subscription instance
        """
        s = self.resp.context['subscription']
        self.assertIsInstance(s, Subscription)
