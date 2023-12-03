from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from apps.core.models import (
    Contact, 
    WebsiteInformation
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'messages_for_email', 'created_at')
    ordering = ('subject', 'created_at')
    search_fields = ('full_name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20

    def messages_for_email(self, obj):
        email = obj.email
        if email:
            url = reverse('admin:core_contact_changelist')
            filtered_url = f"{url}?{urlencode({'email__exact': obj.email})}"
            return format_html('<a href="{}">{}</a>', filtered_url, email)
        return None
    messages_for_email.short_description = "Email"


@admin.register(WebsiteInformation)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('website_name', 'email', 'location', 'tel_number')

