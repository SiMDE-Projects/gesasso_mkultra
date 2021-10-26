from django.contrib import admin
from gesasso.api.models import Action, ActionType, Task, TaskType, Request


@admin.register(ActionType, TaskType, Task, Request)
class CommonAdmin(admin.ModelAdmin):
    pass


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


# class MembershipInline(admin.TabularInline):
#     model = Group.members.through
#
# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#
# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)
