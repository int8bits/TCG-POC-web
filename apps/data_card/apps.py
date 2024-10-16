from django.apps import AppConfig


class DataCardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data_card'

    def ready(self):
        import apps.data_card.signals
