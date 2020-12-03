from django.apps import AppConfig
from django.conf import settings


class ConselheiroConfig(AppConfig):
    name = 'conselheiro'

    def ready(self):
        from .scheduler import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
