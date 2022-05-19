from django.contrib import admin

from gesasso.listener.models import MailRequest


@admin.register(MailRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["mail_subject", "created", "updated"]
    search_fields = ("mail_subject",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.site_header = "Gesasso MK_Ultra"
admin.site.index_title = "Admin"
admin.site.site_title = "Gesasso MK_Ultra"
