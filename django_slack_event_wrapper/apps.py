from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class DjangoSlackeventWrapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_slack_event_wrapper'

    def ready(self):
        # automaticcally install all reciver files
        import django_slack_event_wrapper.custom_signal
        import django_slack_event_wrapper.dispatcher
        import django_slack_event_wrapper.events

        autodiscover_modules('slack')
