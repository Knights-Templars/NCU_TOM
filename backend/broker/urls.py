from django.urls import path
from .views import alerce_targets

urlpatterns = [
    path("alerce/", alerce_targets, name="alerce-targets")
]