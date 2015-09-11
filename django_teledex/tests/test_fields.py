# -*- coding: utf-8 -*-
"""
    teledex.tests.test_fields
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for django-teledex fields.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django_dynamic_fixture import G

from ..models import Address, PhoneNumber, AddressQuerySet, PhoneNumberQuerySet, \
    Email
from ..choices import ADDRESS_STATUS_ACTIVE, ADDRESS_STATUS_INACTIVE, \
    PHONENUMBER_STATUS_ACTIVE, PHONENUMBER_STATUS_INACTIVE
from .testapp.models import ModelWithAddresses, ModelWithPhoneNumbers, \
    ModelWithEmails


class AddressRelationTestCase(TestCase):

    def setUp(self):
        self.obj1 = G(ModelWithAddresses)
        self.obj2 = G(ModelWithAddresses)

        content_type = ContentType.objects.get_for_model(self.obj1)

        self.address1 = G(Address, status=ADDRESS_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.address2 = G(Address, status=ADDRESS_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.address3 = G(Address, status=ADDRESS_STATUS_INACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.address4 = G(Address, status=ADDRESS_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj2.pk)
        self.address5 = G(Address, status=ADDRESS_STATUS_INACTIVE, owner_type=content_type, owner_id=self.obj2.pk)

    def test_relation(self):
        self.assertEqual(Address.objects.count(), 5)

        qs = ModelWithAddresses.objects.filter(addresses=self.address1)
        self.assertEqual(qs.count(), 1)

        qs = ModelWithAddresses.objects.filter(addresses__in=[self.address1, self.address2])
        self.assertEqual(qs.count(), 2)

    def test_relation_active(self):
        qs = ModelWithAddresses.objects.filter(addresses__status=ADDRESS_STATUS_ACTIVE)
        self.assertEqual(qs.count(), 3)

    def test_relation_inactive(self):
        qs = ModelWithAddresses.objects.filter(addresses__status=ADDRESS_STATUS_INACTIVE)
        self.assertEqual(qs.count(), 2)

    def test_reverse_relation(self):
        qs = Address.objects.filter(modelwithaddresses=self.obj1)
        self.assertEqual(qs.count(), 3)
        qs = Address.objects.filter(modelwithaddresses=self.obj1).active()
        self.assertEqual(qs.count(), 2)
        qs = Address.objects.filter(modelwithaddresses=self.obj1).inactive()
        self.assertEqual(qs.count(), 1)
        qs = Address.objects.filter(modelwithaddresses=self.obj2)
        self.assertEqual(qs.count(), 2)


class PhoneNumberRelationTestCase(TestCase):

    def setUp(self):
        self.obj1 = G(ModelWithPhoneNumbers)
        self.obj2 = G(ModelWithPhoneNumbers)

        content_type = ContentType.objects.get_for_model(self.obj1)

        self.phonenumber1 = G(PhoneNumber, status=PHONENUMBER_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.phonenumber2 = G(PhoneNumber, status=PHONENUMBER_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.phonenumber3 = G(PhoneNumber, status=PHONENUMBER_STATUS_INACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.phonenumber4 = G(PhoneNumber, status=PHONENUMBER_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj2.pk)
        self.phonenumber5 = G(PhoneNumber, status=PHONENUMBER_STATUS_INACTIVE, owner_type=content_type, owner_id=self.obj2.pk)

    def test_relation(self):
        self.assertEqual(PhoneNumber.objects.count(), 5)

        qs = ModelWithPhoneNumbers.objects.filter(phonenumbers=self.phonenumber1)
        self.assertEqual(qs.count(), 1)

        qs = ModelWithPhoneNumbers.objects.filter(phonenumbers__in=[self.phonenumber1, self.phonenumber2])
        self.assertEqual(qs.count(), 2)

    def test_relation_active(self):
        qs = ModelWithPhoneNumbers.objects.filter(phonenumbers__status=PHONENUMBER_STATUS_ACTIVE)
        self.assertEqual(qs.count(), 3)

    def test_relation_inactive(self):
        qs = ModelWithPhoneNumbers.objects.filter(phonenumbers__status=PHONENUMBER_STATUS_INACTIVE)
        self.assertEqual(qs.count(), 2)

    def test_reverse_relation(self):
        qs = PhoneNumber.objects.filter(modelwithphonenumbers=self.obj1)
        self.assertEqual(qs.count(), 3)


class EmailRelationTestCase(TestCase):

    def setUp(self):
        self.obj1 = G(ModelWithEmails)
        self.obj2 = G(ModelWithEmails)

        content_type = ContentType.objects.get_for_model(self.obj1)

        self.email1 = G(Email, status=PHONENUMBER_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.email2 = G(Email, status=PHONENUMBER_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.email3 = G(Email, status=PHONENUMBER_STATUS_INACTIVE, owner_type=content_type, owner_id=self.obj1.pk)
        self.email4 = G(Email, status=PHONENUMBER_STATUS_ACTIVE, owner_type=content_type, owner_id=self.obj2.pk)
        self.email5 = G(Email, status=PHONENUMBER_STATUS_INACTIVE, owner_type=content_type, owner_id=self.obj2.pk)

    def test_relation(self):
        self.assertEqual(Email.objects.count(), 5)

        qs = ModelWithEmails.objects.filter(emails=self.email1)
        self.assertEqual(qs.count(), 1)

        qs = ModelWithEmails.objects.filter(emails__in=[self.email1, self.email2])
        self.assertEqual(qs.count(), 2)

    def test_relation_active(self):
        qs = ModelWithEmails.objects.filter(emails__status=PHONENUMBER_STATUS_ACTIVE)
        self.assertEqual(qs.count(), 3)

    def test_relation_inactive(self):
        qs = ModelWithEmails.objects.filter(emails__status=PHONENUMBER_STATUS_INACTIVE)
        self.assertEqual(qs.count(), 2)

    def test_reverse_relation(self):
        qs = Email.objects.filter(modelwithemails=self.obj1)
        self.assertEqual(qs.count(), 3)
