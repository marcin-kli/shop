from django.apps import AppConfig


class ChechoutConfig(AppConfig):
    name = 'chechout'

    def ready(self):
        import checkout.signals
