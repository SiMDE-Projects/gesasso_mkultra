# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    # path("__debug__/", include(debug_toolbar.urls)),
    path("oauth/", include("oauth_pda_app.urls")),
    path("api/", include("gesasso.api.urls")),
    path("proxy_pda/", include("gesasso.proxy_pda.urls")),
    path("listener/", include("gesasso.listener.urls")),
    path("admin/", admin.site.urls),
    re_path(r"", include("gesasso.frontend.urls")),
]
