from django.contrib import admin

from gesasso.listener.models import MailRequest


@admin.register(MailRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["mail_subject", "created", "updated"]
    search_fields = ("mail_subject",)


admin.site.site_header = "Gesasso MK_Ultra"
admin.site.index_title = "Admin"
admin.site.site_title = "Gesasso MK_Ultra"
