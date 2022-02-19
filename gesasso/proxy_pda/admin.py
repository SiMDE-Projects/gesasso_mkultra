from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from gesasso.proxy_pda.models import Asso
from gesasso.proxy_pda.utils import sync_assos


@admin.register(Asso)
class AssoAdmin(admin.ModelAdmin):
    change_list_template = "entities/assos_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("sync/", self.sync),
        ]
        return my_urls + urls

    @csrf_exempt
    def sync(self, request):
        sync_assos(request)
        self.message_user(request, "All assos are now in sync")
        return HttpResponseRedirect("../")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ("login", "shortname", "name", "parent")
    list_filter = (("parent", admin.RelatedOnlyFieldListFilter),)
    search_fields = ("login", "shortname", "name")
    ordering = ("login", "shortname", "name")
