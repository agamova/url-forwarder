from django.contrib import admin
from django.utils.html import format_html

from .models import ForwarderModel


@admin.register(ForwarderModel)
class ForwarderAdmin(admin.ModelAdmin):
    list_display = ("slug", "show_url", "access_code", "redirect_url")

    def show_url(self, obj):
        url = 'yandex.ru/' + obj.slug
        return format_html('<a href="https://{}">{}</a>', url, url)
