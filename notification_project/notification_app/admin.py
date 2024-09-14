from django.contrib import admin
from .models import UserEvent


@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "url", "timestamp")
    list_filter = ("event_type", "timestamp")
    search_fields = ("url",)
