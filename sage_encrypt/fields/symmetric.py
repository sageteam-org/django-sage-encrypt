from django.db import models

from sage_encrypt.mixins.cast import INT, BIGINT, DATE, TIMESTAMP, BOOL, DOUBLE, TIME, NUMERIC
from sage_encrypt.mixins.encrypt import EncryptSymmetricMixin
from sage_encrypt.mixins.query import SYM_ENCRYPT_SQL_WITH_NULLIF


class EncryptedEmailField(EncryptSymmetricMixin, models.EmailField):
    pass


class EncryptedIntegerField(EncryptSymmetricMixin, models.IntegerField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = INT

    def get_internal_type(self):
        return 'IntegerField'


class EncryptedBigIntegerField(EncryptSymmetricMixin, models.BigIntegerField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = BIGINT

    def get_internal_type(self):
        return 'BigIntegerField'


class EncryptedTextField(EncryptSymmetricMixin, models.TextField):
    pass


class EncryptedCharField(EncryptSymmetricMixin, models.CharField):
    pass


class EncryptedDateField(EncryptSymmetricMixin, models.DateField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = DATE

    def get_internal_type(self):
        return 'DateField'


class EncryptedDateTimeField(EncryptSymmetricMixin, models.DateTimeField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = TIMESTAMP

    def get_internal_type(self):
        return 'DateTimeField'


class EncryptedBooleanField(EncryptSymmetricMixin, models.BooleanField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = BOOL

    def get_internal_type(self):
        return 'BooleanField'


class EncryptedFloatField(EncryptSymmetricMixin, models.FloatField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = DOUBLE

    def get_internal_type(self):
        return 'FloatField'


class EncryptedTimeField(EncryptSymmetricMixin, models.TimeField):
    encrypt_query = SYM_ENCRYPT_SQL_WITH_NULLIF
    cast = TIME

    def get_internal_type(self):
        return 'TimeField'

class EncryptedDecimalField(EncryptSymmetricMixin, models.DecimalField):
    cast = NUMERIC

    def get_cast_sql(self):
        return self.cast % {
            'max_digits': self.max_digits,
            'decimal_places': self.decimal_places
        }

    def get_internal_type(self):
        return 'DecimalField'
