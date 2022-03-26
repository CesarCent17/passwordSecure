from django.apps import AppConfig


class GestorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestor'

    def ready(self):
        import gestor.signals
