from django.contrib import admin

from .models import ForwarderModel


@admin.register(ForwarderModel)
class ForwarderAdmin(admin.ModelAdmin):
    list_display = ("slug", "access_code", "redirect_url")


