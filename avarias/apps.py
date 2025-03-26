from django.apps import AppConfig


class AvariasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avarias'
    
    def ready(self):
        import avarias.signals

