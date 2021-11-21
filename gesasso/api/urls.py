from django.urls import include, path
from rest_framework import routers

from gesasso.api import views

api_router = routers.DefaultRouter()
api_router.register(r"users", views.UserViewSet)
api_router.register(r"groups", views.GroupViewSet)
api_router.register(r"assos", views.AssosViewSet)
api_router.register(r"requests", views.RequestViewSet)

urlpatterns = [
    path("", include(api_router.urls)),
    path("me/", views.SelfUserViewSet.as_view({"get": "get"})),
]
