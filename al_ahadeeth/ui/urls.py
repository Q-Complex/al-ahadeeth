"""URLConf for al_ahadeeth.ui"""

from django.urls import path

from al_ahadeeth.ui import views

# Create your URLConf here.
app_name = "al_ahadeeth"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
