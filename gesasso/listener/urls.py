from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MailRequestView, RequestCreatorView

router = DefaultRouter()
router.register(r"mail", MailRequestView)
router.register(r"create", RequestCreatorView, basename="listener-create")

urlpatterns = [
    path("", include(router.urls)),
]
