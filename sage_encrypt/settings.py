from django.conf import settings

ENCRYPT_KEY = settings.ENCRYPT_KEY if hasattr(settings, 'ENCRYPT_KEY') else settings.SECRET_KEY
ENCRYPT_PRIVATE_KEY = settings.ENCRYPT_PRIVATE_KEY if hasattr(settings, 'ENCRYPT_PRIVATE_KEY') else None
ENCRYPT_PUBLIC_KEY = settings.ENCRYPT_PUBLIC_KEY if hasattr(settings, 'ENCRYPT_PUBLIC_KEY') else None
