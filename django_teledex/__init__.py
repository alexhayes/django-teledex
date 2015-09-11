# -*- coding: utf-8 -*-
"""Storage of addresses, phone numbers and emails in Django."""
# :copyright: (c) 2015 Alex Hayes and individual contributors,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.


from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(0, 1, 0, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-teledex'
__docformat__ = 'restructuredtext'

# -eof meta-

from .fields import AddressRelation, PhoneNumberRelation, EmailRelation
from .models import Address, PhoneNumber, Email
from .choices import ADDRESS_STATUS_ACTIVE, ADDRESS_STATUS_INACTIVE, \
    ADDRESS_KIND_POSTAL, ADDRESS_KIND_PHYSICAL, PHONENUMBER_STATUS_ACTIVE, \
    PHONENUMBER_STATUS_INACTIVE, PHONENUMBER_KIND_MOBILE, \
    PHONENUMBER_KIND_WORK, PHONENUMBER_KIND_HOME, PHONENUMBER_KIND_MAIN, \
    PHONENUMBER_KIND_WORKFAX, PHONENUMBER_KIND_HOMEFAX, \
    PHONENUMBER_KIND_GOOGLEVOICE, PHONENUMBER_KIND_PAGER, EMAIL_STATUS_ACTIVE, \
    EMAIL_STATUS_INACTIVE, EMAIL_KIND_WORK, EMAIL_KIND_HOME
