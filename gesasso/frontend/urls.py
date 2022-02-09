from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    url(
        r"^.*/$", views.index
    ),  # regex matches, then lets routing be handled by the frontend. Still needs a / at end.
]
