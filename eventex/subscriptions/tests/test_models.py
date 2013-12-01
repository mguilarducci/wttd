# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
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

    def test_unicode(self):
        self.assertEqual(u'Matheus Guilarducci', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Matheus Guilarducci',
            cpf='01234567890',
            email='email@example.com',
            phone='21-99999-8888'
        )

    def test_cpf_unique(self):
        """
        CPF must be unique
        """
        s = Subscription(
            name='Matheus Guilarducci',
            cpf='01234567890',
            email='outroemail@example.com',
            phone='21-99999-8888'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """
        email must be unique
        """
        s = Subscription(
            name='Matheus Guilarducci',
            cpf='00000000011',
            email='email@example.com',
            phone='21-99999-8888'
        )
        self.assertRaises(IntegrityError, s.save)
