import logging

from django.db import models

from sage_encrypt.collections.asymmetric import ASYMMETRIC_FIELDS
from sage_encrypt.collections.symmetric import SYMMETRIC_FIELDS


def get_encrypted_field(base_class, algorithm='symmetric'):
    """
    get encrypted field for given django field
    :type base_class: models.Field(*args, **kwargs)
    :type algorithm: str
    :rtype: EncryptedField(*args, **kwargs)
    """

    encrypt_fields = {
        'symmetric': SYMMETRIC_FIELDS,
        'asymmetric': ASYMMETRIC_FIELDS
    }

    assert isinstance(base_class, models.Field)
    name, path, args, kwargs = base_class.deconstruct()
    encrypted_field = encrypt_fields.get(algorithm).get(path)

    if encrypted_field:
        if name:
            base_class.__class__ = encrypted_field
            return base_class
        else:
            return encrypted_field(*args, **kwargs)
    else:
        logging.warning(
            'field type {} can not be encrypted in database, ignored'.format(path)
        )
        return base_class


def encrypt_field(base_field, algorithm='symmetric'):
    """
    create EncryptedField for given Field
    :type base_field: models.Field(*args, **kwargs)
    :type algorithm: str (symmetric/asymmetric)
    :rtype: EncryptedField(*args, **kwargs)
    """
    return get_encrypted_field(base_field, algorithm)
