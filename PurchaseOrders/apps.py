from django.apps import AppConfig


class PurchaseordersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PurchaseOrders'

    def ready(self) -> None:
        import PurchaseOrders.signals
