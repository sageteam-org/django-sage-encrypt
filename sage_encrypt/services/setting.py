from django.conf import settings

def get_setting(connection, key):
    """
    get key from connection or default to settings.
    """
    if key in connection.settings_dict:
        return connection.settings_dict[key]
    else:
        return getattr(settings, key)
