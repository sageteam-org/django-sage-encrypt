.. django-sage-encrypt documentation master file, created by
   sphinx-quickstart on Sat Jul  3 00:27:00 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-sage-encrypt's documentation!
===============================================

.. image:: https://sageteamlogo.com
   :target: https://sageteam.org/
   :alt: SageTeam

.. image:: https://sageteamstars.com
   :target: https://github.com/sageteam-org/django-sage-encrypt
   :alt: GitHub

.. image:: https://sageteampypi.com
   :target: https://pypi.org/project/django-sage-encrypt/
   :alt: PyPI release

.. image:: https://sageteampythonversions.com
   :target: https://pypi.org/project/django-sage-encrypt/
   :alt: Supported Python versions

.. image:: https://sageteamdjangoversions.com
   :target: https://pypi.org/project/django-sage-encrypt/
   :alt: Supported Django versions

.. image:: https://sageteamdoc.com
   :target: https://django-sage-encrypt.readthedocs.io/
   :alt: Documentation

.. image:: https://sageteamgithubactions.com
   :target: https://github.com/sageteam-org/django-sage-encrypt
   :alt: GitHub Actions

This app supports the following combinations of Django and Python:

==========  =======================
  Django      Python
==========  =======================
3.1         3.6, 3.7, 3.8, 3.9
3.2         3.6, 3.7, 3.8, 3.9
==========  =======================

Functionality
-------------

Django Sage Encrypt is a tool for using pgcrypto in django.

pgcrypto is an extension for encrypting PostgreSQL at rest, With this module you can increase the security of your sensitive data.

Sage Encrypt supports:

- all database lookups (search, filter, ...)
- symmetric & asymmetric encryption algorithms
- multiple scenarios for preventing data losing

Documentation
-------------

.. toctree::
   :maxdepth: 2

   quick_start
   fields
   secret_key
   commands
   settings

Issues
------

If you have questions or have trouble using the app please file a bug report at:

https://github.com/sageteam-org/django-sage-encrypt/issues



Indices and tables
==================

* :ref:`search`
