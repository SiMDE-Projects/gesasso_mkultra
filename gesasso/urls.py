import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from gesasso.api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"assos", views.AssosViewSet)
router.register(r"actions", views.ActionViewSet)
router.register(r"requests", views.RequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
