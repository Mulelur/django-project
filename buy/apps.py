from django.apps import AppConfig


class BuyConfig(AppConfig):
    name = 'buy'

    def ready(self):
        import buy.signals