from django.urls import path

from .views import GetListAssos
from .views import GetUserInfo

app_name = "proxy_pda"

urlpatterns = [
    path(
        "get_user_infos",
        GetUserInfo.as_view(),
        name="get-user-infos",
    ),
    path(
        "get_list_assos",
        GetListAssos.as_view(),
        name="get_list_assos",
    ),
]
