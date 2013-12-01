# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """
        GET /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        Response should be a rendered template
        """
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """
        HTML must contain input controls
        """
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """
        HTML must contain csrf token
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        Context must have the subscription form
        """
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

