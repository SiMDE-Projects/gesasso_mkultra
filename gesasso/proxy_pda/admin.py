from django.contrib import admin
from django.urls import path

from gesasso.proxy_pda.models import Asso
from gesasso.proxy_pda.utils import sync_assos


@admin.register(Asso)
class AssoAdmin(admin.ModelAdmin):
    change_list_template = "entities/assos_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("sync/", sync_assos),
        ]
        return my_urls + urls
