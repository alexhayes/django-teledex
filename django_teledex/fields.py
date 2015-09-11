# -*- coding: utf-8 -*-
"""
    module.name
    ~~~~~~~~~~~~~~~
    Preamble...
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.contenttypes.fields import GenericRelation


class BaseRelation(GenericRelation):

    def __init__(self, to, related_query_name, **kwargs):
        kwargs['content_type_field'] = 'owner_type'
        kwargs['object_id_field'] = 'owner_id'
        kwargs['related_query_name'] = related_query_name
        super(BaseRelation, self).__init__(to, **kwargs)


class AddressRelation(BaseRelation):

    def __init__(self, related_query_name, **kwargs):
        BaseRelation.__init__(self,
                              'django_teledex.Address',
                              related_query_name,
                              **kwargs)


class PhoneNumberRelation(BaseRelation):

    def __init__(self, related_query_name, **kwargs):
        BaseRelation.__init__(self,
                              'django_teledex.PhoneNumber',
                              related_query_name,
                              **kwargs)


class EmailRelation(BaseRelation):

    def __init__(self, related_query_name, **kwargs):
        BaseRelation.__init__(self,
                              'django_teledex.Email',
                              related_query_name,
                              **kwargs)
