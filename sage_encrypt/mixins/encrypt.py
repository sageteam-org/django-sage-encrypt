from sage_encrypt.mixins.cast import TEXT
from sage_encrypt.mixins.query import SYM_ENCRYPT_SQL, SYM_DECRYPT_SQL
from sage_encrypt.mixins.sql import DecryptedCol

from django.utils.functional import cached_property


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
        value stored in the database is hexadecimal
        """
        return 'bytea'

    def get_placeholder(self, value, compiler, connection):
        """
        tell postgres to encrypt this field using pgcrypto
        """
        raise NotImplementedError('The `get_placeholder` needs to be implemented.')

    def get_cast_sql(self):
        """
        this may be overridden by some implementations
        """
        return self.cast

    def get_decrypt_sql(self, connection):
        """
        get decrypt sql query
        """
        raise NotImplementedError('The `get_decrypt_sql` needs to be implemented.')

    def get_col(self, alias, output_field=None):
        """
        get the decryption for col
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
