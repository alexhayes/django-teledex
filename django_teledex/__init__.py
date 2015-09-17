# -*- coding: utf-8 -*-
"""Storage of addresses, phone numbers and emails in Django."""
# :copyright: (c) 2015 Alex Hayes and individual contributors,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.


from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(0, 2, 0, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-teledex'
__docformat__ = 'restructuredtext'

# -eof meta-

default_app_config = 'django_teledex.apps.DjangoTeledexAppConfig'
#
# from .fields import AddressRelation, PhoneNumberRelation, EmailRelation
# from .models import Address, PhoneNumber, Email
# from .choices import AddressStatus.active, AddressStatus.inactive, \
#     AddressKind.postal, AddressKind.physical, PhoneNumberStatus.active, \
#     PhoneNumberStatus.inactive, PhoneNumberKind,mobile, \
#     PhoneNumberKind.work, PhoneNumberKind.home, PhoneNumberKind.main, \
#     PhoneNumberKind.workFAX, PhoneNumberKind.homeFAX, \
#     PhoneNumberKind.googlevoice, PhoneNumberKind.pager, EmailStatus.active, \
#     EmailStatus.inactive, EmailKind.work, EmailKind.home

