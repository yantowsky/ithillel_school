from django.apps import AppConfig


class MembersAppConfig(AppConfig):
    name = 'members_app'

    def ready(self):
        import members_app.signals  # noqa: F401
