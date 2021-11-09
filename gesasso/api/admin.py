from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.translation import gettext_lazy as _

from gesasso.api.models import Action, ActionType, Task, TaskType, Request, Asso, User
from gesasso.api.views import AssosViewSet


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


@admin.register(Asso)
class AssoAdmin(admin.ModelAdmin):
    change_list_template = "entities/assos_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("sync/", self.sync),
        ]
        return my_urls + urls

    def sync(self, request):
        AssosViewSet.sync_assos()
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


@admin.register(TaskType)
class CommonAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


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


class TaskTypeInline(admin.StackedInline):
    model = Task
    can_delete = False
    extra = 0


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = (
        (None, {"fields": ("username",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    readonly_fields = (
        "last_login",
        "date_joined",
        "is_active",
        "username",
        "first_name",
        "last_name",
        "email",
    )
    ordering = ("last_name", "first_name")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.site_header = "Gesasso MK_Ultra"
admin.site.index_title = "Admin"
admin.site.site_title = "Gesasso MK_Ultra"
