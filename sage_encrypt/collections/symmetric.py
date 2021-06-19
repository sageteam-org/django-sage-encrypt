from sage_encrypt.fields.symmetric import (
    EncryptedCharField,
    EncryptedEmailField,
    EncryptedDateField,
    EncryptedTextField,
    EncryptedFloatField,
    EncryptedDateTimeField,
    EncryptedDecimalField,
    EncryptedBooleanField,
    EncryptedIntegerField,
    EncryptedTimeField,
    EncryptedBigIntegerField
)

SYMMETRIC_FIELDS = {
    'django.db.models.CharField': EncryptedCharField,
    'django.db.models.DateField': EncryptedDateField,
    'django.db.models.DateTimeField': EncryptedDateTimeField,
    'django.db.models.IntegerField': EncryptedIntegerField,
    'django.db.models.BigIntegerField': EncryptedBigIntegerField,
    'django.db.models.EmailField': EncryptedEmailField,
    'django.db.models.TextField': EncryptedTextField,
    'django.db.models.FloatField': EncryptedFloatField,
    'django.db.models.DecimalField': EncryptedDecimalField,
    'django.db.models.BooleanField': EncryptedBooleanField,
    'django.db.models.TimeField': EncryptedTimeField
}
