from django.contrib import admin
from django.contrib.admin.models import LogEntry

from gesasso.api.models import Action, ActionType, Request


@admin.register(LogEntry)
class LogAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = (
        "action_time",
        "user",
        "content_type",
        "object_id",
        "object_repr",
        "action_flag",
        "change_message",
    )


@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["title", "asso", "user", "status", "created", "updated"]
    search_fields = (
        "title",
        "asso",
        "user",
    )


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "Gesasso MK_Ultra"
admin.site.index_title = "Admin"
admin.site.site_title = "Gesasso MK_Ultra"
