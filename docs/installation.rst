============
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

Then place ``django_teledex`` in your ``INSTALLED_APPS``;

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_teledex',
        ...
    )
