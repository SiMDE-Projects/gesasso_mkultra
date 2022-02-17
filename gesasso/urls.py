import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    # path("__debug__/", include(debug_toolbar.urls)),
    path("oauth/", include("oauth_pda_app.urls")),
    path("api/", include("gesasso.api.urls")),
    path("proxy_pda/", include("gesasso.proxy_pda.urls")),
    path("admin/", admin.site.urls),
    re_path("^.*/?$", include("gesasso.frontend.urls")),
]
