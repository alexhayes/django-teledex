==============
django-teledex
==============

Simple storage of addresses, phone numbers and emails in Django_ Models_.


Installation
============

You can install django-teledex either via the Python Package Index (PyPI)
or from github.

To install using pip;

.. code-block:: bash

    $ pip install django-teledex

From github;

.. code-block:: bash

    $ pip install git+https://github.com/alexhayes/django-teledex.git


Usage
=====

Address
-------

.. code-block:: python

    from django_teledex.fields import AddressRelation

    class Company(models.Model):
        addresses = AddressRelation('addresses')


PhoneNumber
-----------

.. code-block:: python

    from django_teledex.fields import PhoneNumberRelation

    class Company(models.Model):
        phone_numbers = PhoneNumberRelation('companies')




License
=======

This software is licensed under the `MIT License`. See the ``LICENSE``
file in the top distribution directory for the full license text.


Author
======

Alex Hayes <alex@alution.com>

.. _`Django`: https://www.djangoproject.com/
.. _`Models`: https://docs.djangoproject.com/en/stable/topics/db/models/
