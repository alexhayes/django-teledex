# -*- coding: utf-8 -*-
"""
    apps.teledex.tests.test_models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for django-teledex models.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.test import TestCase
from django_dynamic_fixture import G, N

from ..models import Address, PhoneNumber, AddressQuerySet, PhoneNumberQuerySet, \
    Email
from ..choices import ADDRESS_STATUS_ACTIVE, ADDRESS_STATUS_INACTIVE, \
    PHONENUMBER_STATUS_ACTIVE, PHONENUMBER_STATUS_INACTIVE, EMAIL_STATUS_ACTIVE, \
    EMAIL_STATUS_INACTIVE


class AddressQuerySetTestCase(TestCase):

    def setUp(self):
        self.address1 = G(Address, status=ADDRESS_STATUS_ACTIVE)
        self.address2 = G(Address, status=ADDRESS_STATUS_ACTIVE)
        self.address3 = G(Address, status=ADDRESS_STATUS_INACTIVE)

    def test_active(self):
        self.assertEqual(Address.objects.active().count(), 2)

    def test_inactive(self):
        self.assertEqual(Address.objects.inactive().count(), 1)

    def test_chain(self):
        self.assertEqual(Address.objects.active().inactive().count(), 0)

    def test_str(self):
        a = N(Address,
              recipient='John Doe',
              organisation='Example',
              address_line='12 Smith St',
              locality='Collingwood',
              region='VIC',
              postcode='3043',
              country='AU')
        """:type : Address"""
        self.assertEqual(str(a), 'John Doe, Example, 12 Smith St, Collingwood VIC 3043, Australia')

        a.organisation = None
        self.assertEqual(str(a), 'John Doe, 12 Smith St, Collingwood VIC 3043, Australia')

        a.address_line = None
        self.assertEqual(str(a), 'John Doe, Collingwood VIC 3043, Australia')

        a.address_line = '12 Smith St'
        a.postcode = None
        self.assertEqual(str(a), 'John Doe, 12 Smith St, Collingwood VIC, Australia')

        a.country = None
        self.assertEqual(str(a), 'John Doe, 12 Smith St, Collingwood VIC')

        a.recipient = None
        self.assertEqual(str(a), '12 Smith St, Collingwood VIC')

        a.address_line = None
        a.locality = None
        self.assertEqual(str(a), 'VIC')

        a.region = None
        self.assertEqual(str(a), '(N/A)')

        a.save()
        self.assertEqual(str(a), '(N/A [%s])' % a.pk)


class PhoneNumberQuerySetTestCase(TestCase):

    def setUp(self):
        self.phonenumber1 = G(PhoneNumber, status=PHONENUMBER_STATUS_ACTIVE)
        self.phonenumber2 = G(PhoneNumber, status=PHONENUMBER_STATUS_ACTIVE)
        self.phonenumber3 = G(PhoneNumber, status=PHONENUMBER_STATUS_INACTIVE)

    def test_active(self):
        self.assertEqual(PhoneNumber.objects.active().count(), 2)

    def test_inactive(self):
        self.assertEqual(PhoneNumber.objects.inactive().count(), 1)

    def test_chain(self):
        self.assertEqual(PhoneNumber.objects.active().inactive().count(), 0)


class EmailQuerySetTestCase(TestCase):

    def setUp(self):
        self.email1 = G(Email, status=EMAIL_STATUS_ACTIVE)
        self.email2 = G(Email, status=EMAIL_STATUS_ACTIVE)
        self.email3 = G(Email, status=EMAIL_STATUS_INACTIVE)

    def test_active(self):
        self.assertEqual(Email.objects.active().count(), 2)

    def test_inactive(self):
        self.assertEqual(Email.objects.inactive().count(), 1)

    def test_chain(self):
        self.assertEqual(Email.objects.active().inactive().count(), 0)
