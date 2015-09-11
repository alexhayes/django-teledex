# -*- coding: utf-8 -*-
"""
    django_teledex.fields
    ~~~~~~~~~~~~~~~~~~~~~

    Defines helper classes used for defining ``GenericRelation`` on models.

    See :doc:`/usage`.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.contenttypes.fields import GenericRelation


class BaseRelation(GenericRelation):
    """
    Helper class useful for automatically setting ``content_type_field`` and ``object_id_field``.
    """

    def __init__(self, to, related_query_name, **kwargs):
        kwargs['content_type_field'] = 'owner_type'
        kwargs['object_id_field'] = 'owner_id'
        kwargs['related_query_name'] = related_query_name
        super(BaseRelation, self).__init__(to, **kwargs)


class AddressRelation(BaseRelation):
    """
    Helper used to map your own model to an :py:class:`django_teledex.models.Address`

    This class can be used to setup the GenericRelation_ between your own model
    and an :py:class:`django_teledex.models.Address`.

    .. _GenericRelation: https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#generic-relations
    """

    def __init__(self, related_query_name, **kwargs):
        """
        :type related_query_name: str
        :param related_query_name:
        """
        BaseRelation.__init__(self,
                              'django_teledex.Address',
                              related_query_name,
                              **kwargs)


class PhoneNumberRelation(BaseRelation):
    """
    Helper used to map your own model to an :py:class:`django_teledex.models.PhoneNumber`

    This class can be used to setup the GenericRelation_ between your own model
    and an :py:class:`django_teledex.models.PhoneNumber`.

    .. _GenericRelation: https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#generic-relations
    """

    def __init__(self, related_query_name, **kwargs):
        BaseRelation.__init__(self,
                              'django_teledex.PhoneNumber',
                              related_query_name,
                              **kwargs)


class EmailRelation(BaseRelation):
    """
    Helper used to map your own model to an :py:class:`django_teledex.models.Email`

    This class can be used to setup the GenericRelation_ between your own model
    and an :py:class:`django_teledex.models.Email`.

    .. _GenericRelation: https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#generic-relations
    """

    def __init__(self, related_query_name, **kwargs):
        BaseRelation.__init__(self,
                              'django_teledex.Email',
                              related_query_name,
                              **kwargs)
