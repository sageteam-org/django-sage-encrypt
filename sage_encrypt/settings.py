from django.conf import settings

ENCRYPT_KEY = settings.ENCRYPT_KEY if hasattr(settings, 'ENCRYPT_KEY') else settings.SECRET_KEY
