from django.urls import include, path
from rest_framework import routers

from gesasso.api import views

api_router = routers.DefaultRouter()
api_router.register(r"users", views.UserViewSet)
api_router.register(r"groups", views.GroupViewSet)
api_router.register(r"assos", views.AssosViewSet)
api_router.register(r"requests", views.RequestViewSet)
api_router.register(r"request_messages", views.RequestMessageViewSet)
api_router.register(r"actions", views.ActionViewSet)
api_router.register(r"action_types", views.ActionTypeViewSet)

urlpatterns = [
    path("", include(api_router.urls)),
]
