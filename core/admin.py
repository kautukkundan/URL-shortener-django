from django.contrib import admin

from core.models import Url

# Register your models here.

@admin.register(Url)
class UrlModel(admin.ModelAdmin):
    fields=['long_url', 'short_url', 'clicks', 'owner']
    list_display = ['id', 'long_url', 'short_url', 'clicks', 'owner']
