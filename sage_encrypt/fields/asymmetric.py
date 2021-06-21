from django.db import models

from sage_encrypt.mixins.cast import INT, BIGINT, DATE, TIMESTAMP, BOOL, DOUBLE, TIME, NUMERIC
from sage_encrypt.mixins.encrypt import EncryptAsymmetricMixin
from sage_encrypt.mixins.query import ASYM_ENCRYPT_SQL_WITH_NULLIF


class EncryptedEmailField(EncryptAsymmetricMixin, models.EmailField):
    pass


class EncryptedIntegerField(EncryptAsymmetricMixin, models.IntegerField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = INT

    def get_internal_type(self):
        return 'IntegerField'


class EncryptedBigIntegerField(EncryptAsymmetricMixin, models.BigIntegerField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = BIGINT

    def get_internal_type(self):
        return 'BigIntegerField'


class EncryptedTextField(EncryptAsymmetricMixin, models.TextField):
    pass


class EncryptedCharField(EncryptAsymmetricMixin, models.CharField):
    pass


class EncryptedDateField(EncryptAsymmetricMixin, models.DateField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = DATE

    def get_internal_type(self):
        return 'DateField'


class EncryptedDateTimeField(EncryptAsymmetricMixin, models.DateTimeField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = TIMESTAMP

    def get_internal_type(self):
        return 'DateTimeField'


class EncryptedBooleanField(EncryptAsymmetricMixin, models.BooleanField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = BOOL

    def get_internal_type(self):
        return 'BooleanField'


class EncryptedFloatField(EncryptAsymmetricMixin, models.FloatField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = DOUBLE

    def get_internal_type(self):
        return 'FloatField'


class EncryptedTimeField(EncryptAsymmetricMixin, models.TimeField):
    encrypt_query = ASYM_ENCRYPT_SQL_WITH_NULLIF
    cast = TIME

    def get_internal_type(self):
        return 'TimeField'

class EncryptedDecimalField(EncryptAsymmetricMixin, models.DecimalField):
    cast = NUMERIC

    def get_cast_sql(self):
        return self.cast % {
            'max_digits': self.max_digits,
            'decimal_places': self.decimal_places
        }

    def get_internal_type(self):
        return 'DecimalField'
