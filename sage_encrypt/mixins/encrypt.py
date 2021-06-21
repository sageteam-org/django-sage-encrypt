from sage_encrypt.mixins.cast import TEXT
from sage_encrypt.mixins.query import (
    SYM_ENCRYPT_SQL,
    SYM_DECRYPT_SQL,
    ASYM_ENCRYPT_SQL,
    ASYM_DECRYPT_SQL
)
from sage_encrypt.mixins.sql import DecryptedCol

from django.utils.functional import cached_property

from sage_encrypt.services.setting import get_setting


class Encrypt:
    """
    PostgreSQL pgcrypto encryption for django fields
    """
    encrypt_query = None
    decrypt_query = None
    cast = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def db_type(self, connection=None):
        """
        value stored in database is hexadecimal
        :param connection: connection object
        :type connection: object
        :return: db type
        :rtype: str
        """
        return 'bytea'

    def get_placeholder(self, value, compiler, connection):
        """
        tell postgres to encrypt this field using pgcrypto
        :return: encrypt sql query
        :rtype: str
        """
        raise NotImplementedError('The `get_placeholder` needs to be implemented.')

    def get_cast_sql(self):
        """
        this may be overridden by some implementations
        :return: cast type
        :rtype: str
        """
        return self.cast

    def get_decrypt_sql(self, connection):
        """
        get decrypt sql query
        :param connection: connection object
        :type connection: object
        :return: decrypt sql query
        :rtype: str
        """
        raise NotImplementedError('The `get_decrypt_sql` needs to be implemented.')

    def get_col(self, alias, output_field=None):
        """
        get the decryption for col
        :return: db col
        :rtype: DecryptedCol
        """
        if output_field is None:
            output_field = self
        if alias != self.model._meta.db_table or output_field != self:
            return DecryptedCol(
                alias,
                self,
                output_field
            )
        else:
            return self.cached_col

    @cached_property
    def cached_col(self):
        """
        get cached version of decryption for col
        """
        return DecryptedCol(
            self.model._meta.db_table,
            self
        )

class EncryptSymmetricMixin(Encrypt):
    """
    pgcrypto symmetric key encrypted field mixin
    """
    encrypt_query = SYM_ENCRYPT_SQL
    decrypt_query = SYM_DECRYPT_SQL
    cast = TEXT

    def get_placeholder(self, value, compiler, connection):
        """
        set encrypt key
        :return: encrypt sql query
        :rtype: str
        """
        return self.encrypt_query.format(get_setting(connection, 'ENCRYPT_KEY'))

    def get_decrypt_sql(self, connection):
        """
        set decrypt key
        :param connection: connection object
        :type connection: object
        :return: decrypt sql query
        :rtype: str
        """
        return self.decrypt_query.format(get_setting(connection, 'ENCRYPT_KEY'))

    def get_internal_type(self):
        """
        may be overridden by some implementations
        :return: field type
        :rtype: str
        """
        return 'BinaryField'

class EncryptAsymmetricMixin(Encrypt):
    """
    pgcrypto asymmetric key encrypted field mixin
    """
    encrypt_query = ASYM_ENCRYPT_SQL
    decrypt_query = ASYM_DECRYPT_SQL
    cast = TEXT

    def get_placeholder(self, value=None, compiler=None, connection=None):
        """
        set encrypt key
        :return: encrypt sql query
        :rtype: str
        """
        return self.encrypt_query.format(get_setting(connection, 'ENCRYPT_PUBLIC_KEY'))

    def get_decrypt_sql(self, connection):
        """
        set decrypt key
        :param connection: connection object
        :type connection: object
        :return: decrypt sql query
        :rtype: str
        """
        return self.decrypt_query.format(get_setting(connection, 'ENCRYPT_PRIVATE_KEY'))

    def get_internal_type(self):
        """
        may be overridden by some implementations
        :return: field type
        :rtype: str
        """
        return 'BinaryField'
