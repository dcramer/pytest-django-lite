A minimal plugin to integration Django and py.test.

Usage
=====

Install the plugin:

::

    pip install pytest-django-lite


Configuring Django
==================

You have two options to configure your testsuite's Django settings.

1. Create a conftest.py
-----------------------

.. code:: python

    def pytest_configure(config):
        from django.conf import settings

        settings.configure(
            DATABASES={},
            INSTALLED_APPS=[],
            # etc
        )


2. Pass DJANGO_SETTINGS_MODULE

::
    DJANGO_SETTINGS_MODULE=myapp.settings py.test


Credits
=======

This was originally based on `pytest-django <https://github.com/pelme/pytest_django>`_.