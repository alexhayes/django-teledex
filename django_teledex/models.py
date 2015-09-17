# -*- coding: utf-8 -*-
"""
    teledex.models
    ~~~~~~~~~~~~~~

    Django models for django-teledex.

"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers
from django.conf import settings
# todo Make reversion support optional detecting import failure and faking the decorator
import reversion

from .choices import AddressKind, AddressStatus, PhoneNumberKind, \
    PhoneNumberStatus, EmailKind, EmailStatus


class AddressQuerySet(models.QuerySet):
    """
    Address QuerySet.
    """

    def active(self):
        """
        Filter for active Addresses

        :rtype: AddressQuerySet
        """
        return self.filter(status=AddressStatus.active)

    def inactive(self):
        """
        Filter for inactive Addresses

        :rtype: AddressQuerySet
        """
        return self.filter(status=AddressStatus.inactive)

    def kind(self, kind):
        """
        Filter addresses by a particular kind.

        Accepts any of the

        :rtype: AddressQuerySet
        """
        return self.filter(kind=kind)

    def postal(self):
        """
        Filter for postal addresses.

        :rtype: AddressQuerySet
        """
        return self.kind(AddressKind.postal)

    def physical(self):
        """
        Filter for physical addresses.

        :rtype: AddressQuerySet
        """
        return self.kind(AddressKind.physical)


@reversion.register
class Address(models.Model):
    """
    Defines an Address.

    Sigh... if only we had a port of
    `libaddressinput <https://github.com/googlei18n/libaddressinput>`_
    in Python... :(
    """
    kind = models.CharField(_('kind'), max_length=16, choices=AddressKind.choices, default=AddressKind.postal, db_index=True, help_text=_('The kind of address'))
    status = models.CharField(_('status'), max_length=16, choices=AddressStatus.choices, db_index=True, default=AddressStatus.active, help_text="Defines the current status of the address")
    # Actual address fields
    recipient = models.CharField(_('recipient'), max_length=255, null=True, blank=True, help_text=_('Recipient'))
    organisation = models.CharField(_('organisation'), max_length=255, null=True, blank=True, help_text=_('Organisation'))
    address_line = models.CharField(_('address'), max_length=255, null=True, help_text=_('Street address lines separated by commas (,)'))
    locality = models.CharField(_('locality'), max_length=255, null=True, help_text=_('City or town'))
    region = models.CharField(_('region'), max_length=128, null=True, help_text=_('State code, country or canton'))
    postcode = models.CharField(_('postcode'), max_length=32, null=True, help_text=_('Postal code, post code ZIP code'))
    country = CountryField(_('country'), db_index=True, null=True)
    # Defines something that this address belongs to
    owner_type = models.ForeignKey(ContentType, null=True, blank=True)
    owner_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    owner = GenericForeignKey('owner_type', 'owner_id')

    objects = AddressQuerySet.as_manager()

    class Meta:
        index_together = [
            ['owner_type', 'owner_id']
        ]

    def __str__(self):
        """
        Return a string representation of the address.

        This is very basic and somewhat Australian (at least until proven
        otherwise...)
        """
        s = self.joined()
        if len(s) > 0:
            return s
        elif self.pk:
            return '(N/A [%s])' % self.pk
        else:
            return '(N/A)'

    def joined(self):
        """
        Join the address into a single line string separated by commas.

        :rtype: str
        """
        # todo Perhaps needs to be formatted according to the country...
        parts = [self.recipient,
                 self.organisation,
                 self.address_line,
                 ' '.join([part
                           for part in [self.locality, self.region, self.postcode]
                           if part is not None and len(part) > 0]),
                 str(self.country.name) if self.country else None]
        s = ', '.join([part
                       for part in parts
                       if part is not None and len(part) > 0])
        return s


class PhoneNumberQuerySet(models.QuerySet):
    """
    PhoneNumber QuerySet.
    """

    def active(self):
        """
        Filter for active Phone Numbers
        """
        return self.filter(status=PhoneNumberStatus.active)

    def inactive(self):
        """
        Filter for inactive Phone Numbers
        """
        return self.filter(status=PhoneNumberStatus.inactive)

    def kind(self, kind):
        return self.filter(kind=kind)


@reversion.register
class PhoneNumber(models.Model):
    """
    Defines a Phone Number.
    """
    kind = models.CharField(_('kind'), max_length=16, choices=PhoneNumberKind.choices, default=PhoneNumberKind.work, db_index=True, help_text=_('The kind of phone number'))
    status = models.CharField(_('status'), max_length=16, choices=PhoneNumberStatus.choices, default=PhoneNumberStatus.active, db_index=True, help_text="Defines the current status of the phone number")
    # Actual Phone Number
    number = PhoneNumberField(max_length=40, db_index=True)
    # Defines something that this address belongs to
    owner_type = models.ForeignKey(ContentType, null=True, blank=True)
    owner_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    owner = GenericForeignKey('owner_type', 'owner_id')

    objects = PhoneNumberQuerySet.as_manager()

    class Meta:
        index_together = [
            ['owner_type', 'owner_id']
        ]

    def __str__(self):
        return '%s' % self.number


class EmailQuerySet(models.QuerySet):
    """
    Email QuerySet.
    """

    def active(self):
        """
        Filter for active Phone Numbers
        """
        return self.filter(status=EmailStatus.active)

    def inactive(self):
        """
        Filter for inactive Phone Numbers
        """
        return self.filter(status=EmailStatus.inactive)

    def kind(self, kind):
        return self.filter(kind=kind)


@reversion.register
class Email(models.Model):
    """
    Defines a Phone Number.
    """
    kind = models.CharField(_('kind'), max_length=16, choices=EmailKind.choices, default=EmailKind.work, db_index=True, help_text=_('The kind of email'))
    status = models.CharField(_('status'), max_length=16, choices=EmailStatus.choices, default=EmailStatus.active, db_index=True, help_text="Defines the current status of the email")
    # Actual Phone Number
    email = models.EmailField(max_length=191, db_index=True)
    # Defines something that this address belongs to
    owner_type = models.ForeignKey(ContentType, null=True, blank=True)
    owner_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    owner = GenericForeignKey('owner_type', 'owner_id')

    objects = EmailQuerySet.as_manager()

    class Meta:
        index_together = [
            ['owner_type', 'owner_id']
        ]

    def __str__(self):
        return '%s' % self.email
