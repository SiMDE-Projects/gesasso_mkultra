from django.contrib import admin
from gesasso.api.models import Action, ActionType, Task, TaskType, Request, Asso


@admin.register(ActionType, TaskType, Task, Asso)
class CommonAdmin(admin.ModelAdmin):
    pass


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(RequestAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['asso'].label_from_instance = lambda obj: "{} ({})".format(obj.login, obj.shortname)
        form.base_fields['type'].label_from_instance = lambda obj: obj.name
        return form


class TaskTypeInline(admin.StackedInline):
    model = Task
    can_delete = False
    extra = 0


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    def get_actiontype_name(self):
        print(self.type.__dict__)
        return self.type.name

    def get_queryset(self, request):
        print(super().get_queryset(request).select_related("type"))
        return super().get_queryset(request).select_related("type")

    list_display = ("name", get_actiontype_name, "created", "updated")
    pass
