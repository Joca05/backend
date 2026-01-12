from django.apps import AppConfig


class InventoryConfig(AppConfig):
    name = 'receita'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import receita.signals
