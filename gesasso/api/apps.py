from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gesasso.api"
    verbose_name = "Gesasso API"
    app_label = "Listener Gesasso"
