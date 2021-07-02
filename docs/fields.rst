Fields
------

For encrypting each row of your database there are multiple ways:

1. use ``encrypt_field`` function in your models.py

.. code:: python

    from django.db import models
    from sage_encrypt.services.encrypt import encrypt_field

    # symmetric encryption
    title = encrypt_field(models.CharField(max_length=255))

    # asymmetric encryption
    title = encrypt_field(models.CharField(max_length=255), algorithm='asymmetric')

2. use field directly

.. code:: python

    # symmetric encryption
    from sage_encrypt.fields.symmetric import EncryptedCharField

    title = EncryptedCharField(max_length=255)


    # asymmetric encryption
    from sage_encrypt.fields.asymmetric import EncryptedCharField

    title = EncryptedCharField(max_length=255)

If you want to use ``symmetric encryption`` you don't need to generate
secret keys default is SECRET\_KEY

But if you want to use ``asymmetric encryption`` you have to generate
private key & public key