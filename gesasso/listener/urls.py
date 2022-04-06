from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TriageRequestView

router = DefaultRouter()
router.register(r"listener", TriageRequestView, basename="listener")

urlpatterns = [
    # path(
    #     "requesttriage",
    #     CreateTriageRequest.as_view(),
    #     name="create-triage-request",
    # ),
    path(
        "get",
        TriageRequestView,
        name="create-triage-request",
    ),
]
