# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Matheus Guilarducci',
            cpf='01234567890',
            email='email@example.com',
            phone='21-99999-8888'
        )

    def test_create(self):
        """
        Subscription must have name, cpf, email and phone
        """
        self.obj.save()
        self.assertEqual(1,self.obj.pk)

    def test_has_created_at(self):
        """
        Subscription must have automatic created_at
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)
