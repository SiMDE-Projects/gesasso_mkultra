from django.urls import include, path
from rest_framework import routers
from gesasso.api import views
from django.contrib import admin
import debug_toolbar


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"assos", views.AssosViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
