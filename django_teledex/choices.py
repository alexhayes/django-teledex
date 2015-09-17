# -*- coding: utf-8 -*-
"""
    django_teledex.choices
    ~~~~~~~~~~~~~~~~~~~~~~

    Define choices that can be used within django-teledex.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.utils.translation import ugettext_lazy as _
from djchoices import DjangoChoices, ChoiceItem


class AddressStatus(DjangoChoices):
    """
    Defines statues used for :py:attr:`django_teledex.models.Address.status`
    """
    active = ChoiceItem()
    inactive = ChoiceItem()


class AddressKind(DjangoChoices):
    """
    Defines statues used for :py:attr:`django_teledex.models.Address.kind`
    """
    postal = ChoiceItem()
    physical = ChoiceItem()


class PhoneNumberStatus(DjangoChoices):
    """
    Defines statues used for :py:attr:`django_teledex.models.PhoneNumber.status`
    """
    active = ChoiceItem()
    inactive = ChoiceItem()


class PhoneNumberKind(DjangoChoices):
    """
    Defines statues used for :py:attr:`django_teledex.models.PhoneNumber.kind`
    """
    mobile = ChoiceItem()
    work = ChoiceItem()
    home = ChoiceItem()
    main = ChoiceItem()
    workfax = ChoiceItem('workfax', 'work fax')
    homefax = ChoiceItem('homefax', 'home fax')
    googlevoice = ChoiceItem('googlevoice', 'google voice')
    pager = ChoiceItem()


class EmailStatus(DjangoChoices):
    """
    Defines statues used for :py:attr:`django_teledex.models.Email.status`
    """
    active = ChoiceItem()
    inactive = ChoiceItem()


class EmailKind(DjangoChoices):
    """
    Defines statues used for :py:attr:`django_teledex.models.Email.kind`
    """
    work = ChoiceItem()
    home = ChoiceItem()
