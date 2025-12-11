"""AppConf for al_ahadeeth.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for al_ahadeeth.api"""

    name = "al_ahadeeth.api"
    label = "al_ahadeeth_api"
    default_auto_field = "django.db.models.BigAutoField"
