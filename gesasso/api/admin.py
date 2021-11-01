from django.contrib import admin
from django.contrib.admin.models import LogEntry

from gesasso.api.models import Action, ActionType, Task, TaskType, Request, Asso, User


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
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ("login", "shortname", "name", "parent")


@admin.register(TaskType)
class CommonAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["type"].label_from_instance = lambda o: o.name
        return form


@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["tasks_types"].label_from_instance = lambda o: o.name
        return form


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["actions"].label_from_instance = lambda o: "{} ({})".format(
            o.name, o.type.name
        )
        return form

    def user_name(self, obj):
        return "{} {}".format(obj.user, obj.user)

    list_display = ["title", "asso", "user_name", "status", "created", "updated"]


class TaskTypeInline(admin.StackedInline):
    model = Task
    can_delete = False
    extra = 0


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["type"].label_from_instance = lambda o: o.name
        return form


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "Gesasso MK_Ultra"
admin.site.index_title = "Admin"
admin.site.site_title = "Gesasso MK_Ultra"
