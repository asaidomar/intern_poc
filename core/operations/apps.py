from django.apps import AppConfig



class OperationsConfig(AppConfig):
    name = 'core.operations'

    def ready(self):
        import core.operations.signals
        return super().ready()