"""AppConf for al_ahadeeth.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for al_ahadeeth.cms"""

    name = "al_ahadeeth.cms"
    label = "al_ahadeeth_cms"
    default_auto_field = "django.db.models.BigAutoField"
