from django.apps import AppConfig


class IpLocatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ip_locator'

    # def ready(self):
    #     from . import signals
