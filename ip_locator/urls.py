from django.urls import path, re_path
from . import views



urlpatterns = [
    path("locator/", views.locator.as_view(), name="locator"),
    path("getapikey/", views.GetAPiKey.as_view(), name="getapikey"),
]