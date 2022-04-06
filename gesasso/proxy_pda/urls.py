from django.urls import path

from gesasso.proxy_pda import views

urlpatterns = [
    path(
        "get_user_infos",
        views.GetUserInfo.as_view(),
        name="get_user_infos",
    ),
    path(
        "get_assos_list",
        views.GetListAssos.as_view(),
        name="get_assos_list",
    ),
]
