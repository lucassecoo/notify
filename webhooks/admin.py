from django.contrib import admin
from webhooks.models import Webhook

@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type', 'created_at')
    list_filter = ('event_type',)
