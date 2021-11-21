import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("front/", include("gesasso.frontend.urls")),
    path("api/", include("gesasso.api.urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
