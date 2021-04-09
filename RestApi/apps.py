from django.apps import AppConfig
class RestApiconfig(AppConfig):
    name="RestApi"
    def ready(self):
        from . import signals