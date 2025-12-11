"""AppConf for al_ahadeeth.ui"""

from django.apps import AppConfig


# Create your config here.
class UIConfig(AppConfig):
    """App configuration for al_ahadeeth.ui"""

    name = "al_ahadeeth.ui"
    label = "app_ui"
    default_auto_field = "django.db.models.BigAutoField"
