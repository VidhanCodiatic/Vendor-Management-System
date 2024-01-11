from django.apps import AppConfig


class VendorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Vendors'

    def ready(self) -> None:
        import Vendors.signals