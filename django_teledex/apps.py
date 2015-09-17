# -*- coding: utf-8 -*-
"""
    teledex.apps
    ~~~~~~~~~~~~

    Defines the Django application teledex.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.apps import AppConfig


class DjangoTeledexAppConfig(AppConfig):
    name = 'django_teledex'
    label = 'django_teledex'
    verbose_name = 'Django Teledex'
