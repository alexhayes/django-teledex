# -*- coding: utf-8 -*-
"""
    apps.selectpt.core.admin
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
import reversion
from .models import Address, PhoneNumber, Email


class AddressAdmin(reversion.VersionAdmin):
    pass


class PhoneNumberAdmin(reversion.VersionAdmin):
    pass


class EmailAdmin(reversion.VersionAdmin):
    pass


admin.site.register(Address, AddressAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Email, EmailAdmin)
