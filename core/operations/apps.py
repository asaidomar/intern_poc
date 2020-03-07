from django.apps import AppConfig


class OperationsConfig(AppConfig):
    name = 'core.operations'

    def ready(self):
        import core.operations.signals  # noqa
        return super().ready()
