from django.urls import include, path

from gesasso.api import views
from gesasso.api.utils import DefaultRouter
from gesasso.listener.urls import router as listener_router

api_router = DefaultRouter()
api_router.register(r"users", views.UserViewSet)
api_router.register(r"groups", views.GroupViewSet)
api_router.register(r"assos", views.AssosViewSet)
api_router.register(r"requests", views.RequestViewSet)
api_router.register(r"request_messages", views.RequestMessageViewSet)
api_router.register(r"actions", views.ActionViewSet)
api_router.register(r"action_types", views.ActionTypeViewSet)
api_router.extend(listener_router)

urlpatterns = [
    path("", include(api_router.urls)),
]
