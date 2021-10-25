from django.urls import include, path
from rest_framework import routers
from gesasso.api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
