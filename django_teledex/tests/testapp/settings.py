# -*- coding: utf-8 -*-
"""
    module.name
    ~~~~~~~~~~~~~~~
    Preamble...
"""
from __future__ import absolute_import, print_function, unicode_literals
import json

# TEST SETTINGS
import random

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Django replaces this, but it still wants it. *shrugs*
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django_teledex',
    'django_teledex.tests.testapp',
)

MIDDLEWARE_CLASSES = {}

NOSE_ARGS=[
    '--logging-clear-handlers',
    # Coverage - turn on with NOSE_WITH_COVERAGE=1
    '--cover-html',
    '--cover-package=django_teledex',
    '--cover-erase',
    '--with-fixture-bundling',
    # Nose Progressive
    '--with-progressive',
]

SECRET_KEY = '53cr3773rc3553cr3773rc3553cr3773rc3553cr3773rc35'

DDF_FIELD_FIXTURES = {
    'phonenumber_field.modelfields.PhoneNumberField': {
        'ddf_fixture': lambda: '+61400%s' % random.randint(100000, 999999)
    },
}
