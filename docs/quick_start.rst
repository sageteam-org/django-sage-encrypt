Installation
------------

First install package

.. code:: shell

    $ pip install django-sage-encrypt

Then add 'sage\_encrypt' to INSTALLED\_APPS in settings.py

.. code:: python

    INSTALLED_APPS = [
      ...
      'sage_encrypt',
      ...
    ]

Also you need to install ``pgcrypto`` extension in your database:

.. code:: shell

    sudo -u postgres psql <db_name>

.. code:: postgresql

    CREATE EXTENSION pgcrypto;