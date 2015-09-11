# -*- coding: utf-8 -*-
"""
    django_teledex.choices
    ~~~~~~~~~~~~~~~~~~~~~~

    Define choices that can be used within django-teledex.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.utils.translation import ugettext_lazy as _


ADDRESS_STATUS_ACTIVE = 'active'
ADDRESS_STATUS_INACTIVE = 'inactive'
ADDRESS_STATUS_CHOICES = (
    (ADDRESS_STATUS_ACTIVE, _('active')),
    (ADDRESS_STATUS_INACTIVE, _('inactive')),
)

ADDRESS_KIND_POSTAL = 'postal'
ADDRESS_KIND_PHYSICAL = 'physical'
ADDRESS_KIND_CHOICES = (
    (ADDRESS_KIND_POSTAL, _('postal')),
    (ADDRESS_KIND_PHYSICAL, _('physical')),
)

PHONENUMBER_STATUS_ACTIVE = 'active'
PHONENUMBER_STATUS_INACTIVE = 'inactive'
PHONENUMBER_STATUS_CHOICES = (
    (PHONENUMBER_STATUS_ACTIVE, _('active')),
    (PHONENUMBER_STATUS_INACTIVE, _('inactive')),
)

PHONENUMBER_KIND_MOBILE = 'mobile'
PHONENUMBER_KIND_WORK = 'work'
PHONENUMBER_KIND_HOME = 'home'
PHONENUMBER_KIND_MAIN = 'main'
PHONENUMBER_KIND_WORKFAX = 'workfax'
PHONENUMBER_KIND_HOMEFAX = 'homefax'
PHONENUMBER_KIND_GOOGLEVOICE = 'googlevoice'
PHONENUMBER_KIND_PAGER = 'pager'
PHONENUMBER_KIND_CHOICES = (
    (PHONENUMBER_KIND_MOBILE, _('mobile')),
    (PHONENUMBER_KIND_WORK, _('work')),
    (PHONENUMBER_KIND_HOME, _('home')),
    (PHONENUMBER_KIND_MAIN, _('main')),
    (PHONENUMBER_KIND_WORKFAX, _('work fax')),
    (PHONENUMBER_KIND_HOMEFAX, _('home fax')),
    (PHONENUMBER_KIND_GOOGLEVOICE, _('google voice')),
    (PHONENUMBER_KIND_PAGER, _('pager')),
)

EMAIL_STATUS_ACTIVE = 'active'
EMAIL_STATUS_INACTIVE = 'inactive'
EMAIL_STATUS_CHOICES = (
    (EMAIL_STATUS_ACTIVE, _('active')),
    (EMAIL_STATUS_INACTIVE, _('inactive')),
)

EMAIL_KIND_WORK = 'work'
EMAIL_KIND_HOME = 'home'
EMAIL_KIND_CHOICES = (
    (EMAIL_KIND_WORK, _('work')),
    (EMAIL_KIND_HOME, _('home')),
)
