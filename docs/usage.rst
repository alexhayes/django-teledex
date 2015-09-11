Usage
=====

There are three models Address, PhoneNumber and Email which all present
essentially the same API.

For the examples below let's assume you have the following model;

.. code-block:: python

    # models.py

    from django.db import models
    from django_teledex import AddressRelation, PhoneNumberRelation, EmailRelation


    class Company(models.Model):
        title = models.CharField(max_length=100)
        addresses = AddressRelation('companies')
        phonenumbers = PhoneNumberRelation('companies')
        emails = EmailRelation('companies')


Address
-------

If you want to add an address you can then do the following;

.. code-block:: python

    from django_teledex import Address, ADDRESS_KIND_PHYSICAL

    company = Company.objects.create(title='Evelyn Hotel')

    address = Address.objects.create(
        organisation=company.title,
        kind=ADDRESS_KIND_PHYSICAL,
        owner=company,
        address_line='351 Brunswick St',
        locality='Fitzroy',
        region='VIC',
        postcode='3065',
        country='AU',
    )

    company.addresses.all() # returns all addresses for company
    company.addresses.active() # all active addresses

    # Make an address inactive
    address.deactivate()

    company.addresses.inactive() # all inactive addresses
    company.addresses.kind(ADDRESS_KIND_PHYSICAL) # get addresses by kind
    company.addresses.filter(postcode=3065) # filter works as you'd expect...

    # Make an address active
    address.activate()


A complete list of QuerySet methods available on ``Address.objects`` is available
in :py:class:`django_teledex.models.AddressQuerySet`.


PhoneNumber
-----------

The :code:`PhoneNumber` model behaves in pretty much the same way, for example;

.. code-block:: python

    from django_teledex import PhoneNumber, PHONENUMBER_KIND_MOBILE

    company = Company.objects.create(title='Evelyn Hotel')

    phonenumber = PhoneNumber.objects.create(
        kind=PHONENUMBER_KIND_MOBILE,
        owner=company,
        number='+61 3 9419 5500'
    )

    company.phonenumbers.all() # returns all phone numbers for company
    company.phonenumbers.active() # all active phone numbers

    # Make an phone number inactive
    phonenumber.deactivate()

    company.phonenumbers.inactive() # all inactive addresses
    company.phonenumbers.kind(PHONENUMBER_KIND_MOBILE) # by kind
    company.phonenumbers.filter(kind=PHONE) # filter works as you'd expect...

    # Make an phone number active
    phonenumber.activate()


A complete list of QuerySet methods available on ``PhoneNumber.objects`` is available
in :py:class:`django_teledex.models.PhoneNumberQuerySet`.


Validation
``````````

:code:`PhoneNumber` is a :code:`PhoneNumberField` which comes from
`django-phonenumber-field <https://github.com/stefanfoulis/django-phonenumber-field>`_
which;

    is a library which interfaces with python-phonenumbers to validate,
    pretty print and convert phone numbers. :code:`python-phonenumbers` is a
    port of Google's `libphonenumber <https://code.google.com/p/libphonenumber/>`_
    library, which powers Android's phone number handling.

You'll probably want to look into the above to get familiar with how they are
useful to your project.


Email
-----

The :code:`Email` model also behaves in pretty much the same way, for example;

.. code-block:: python

    from django_teledex import Email, EMAIL_KIND_WORK

    company = Company.objects.create(title='Evelyn Hotel')

    email = Email.objects.create(
        kind=EMAIL_KIND_WORK,
        owner=company,
        email='guys@example.com'
    )

    company.emails.all() # returns all phone numbers for company
    company.emails.active() # all active phone numbers

    # Make an phone number inactive
    email.deactivate()

    company.emails.inactive() # all inactive addresses
    company.emails.kind(EMAIL_KIND_WORK) # by kind
    company.emails.filter(email__icontains='guys@') # filter works as you'd expect...

    # Make an phone number active
    email.activate()


A complete list of QuerySet methods available on ``Email.objects`` is available
in :py:class:`django_teledex.models.EmailQuerySet`.



Reverse Relations
-----------------

You can also traverse back from an ``Address``, ``PhoneNumber`` or
``Email`` to the owner, in this case the ``Company`` - all thanks to Django's
`reverse generic relations`_.

:py:class:`django_teledex.fields.AddressRelation`, :py:class:`django_teledex.fields.PhoneNumberRelation`
and :py:class:`django_teledex.fields.EmailRelation` are simply helper classes
that inherit from `GenericRelation`_ that set some defaults.

The first, and only required, argument to each of the ``*Relation`` classes is
the `related_query_name`_ used by the GenericRelation_ which
:py:class:`django_teledex.fields.AddressRelation`,
:py:class:`django_teledex.fields.PhoneNumberRelation` and
:py:class:`django_teledex.fields.EmailRelation` inherit from. In the
``Company`` model above it's set to ``companies``.

Thus;

.. code-block:: python

    # Reverse relations
    Address.objects.filter(companies__title='Evelyn Hotel')


.. _reverse generic relations: https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#reverse-generic-relations
.. _related_query_name: https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation.related_query_name
.. _GenericRelation: https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation
