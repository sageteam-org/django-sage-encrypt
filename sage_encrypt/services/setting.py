from sage_encrypt import settings

def get_setting(connection, key):
    """
    get key from connection or default to settings.
    :type connection
    :type key: str
    :rtype setting value
    """
    if key in connection.settings_dict:
        return connection.settings_dict[key]
    else:
        return getattr(settings, key)
