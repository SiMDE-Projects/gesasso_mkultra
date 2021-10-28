from django.contrib import admin
from gesasso.api.models import Action, ActionType, Task, TaskType, Request, Asso


@admin.register(TaskType, Asso)
class CommonAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(self.__class__, self).get_form(request, obj, **kwargs)
        form.base_fields['type'].label_from_instance = lambda o: o.name
        return form


@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(self.__class__, self).get_form(request, obj, **kwargs)
        form.base_fields['tasks_types'].label_from_instance = lambda o: o.name
        return form


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(self.__class__, self).get_form(request, obj, **kwargs)
        form.base_fields['asso'].label_from_instance = lambda o: "{} ({})".format(o.login, o.shortname)
        form.base_fields['actions'].label_from_instance = lambda o: "{} ({})".format(o.name, o.type.name)
        return form

    def asso_name(self, obj):
        return "{} ({})".format(obj.asso.shortname, obj.asso.login)

    def user_name(self, obj):
        return "{} {}".format(obj.user, obj.user)

    list_display = ['title', 'asso_name', 'user_name', 'status', 'created', 'updated']


class TaskTypeInline(admin.StackedInline):
    model = Task
    can_delete = False
    extra = 0


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(self.__class__, self).get_form(request, obj, **kwargs)
        form.base_fields['type'].label_from_instance = lambda o: o.name
        return form


admin.site.site_header = 'Gesasso MK_Ultra'  # default: "Django Administration"
admin.site.index_title = 'Admin'  # default: "Site administration"
admin.site.site_title = 'Gesasso MK_Ultra'  # default: "Django site admin"
