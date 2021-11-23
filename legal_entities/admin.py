from django.contrib import admin
from legal_entities.models import LegalEntity

from clients.models import Client
class LegalEntityAdmin(admin.ModelAdmin):
    inlines = [
        Client,
    ]
    list_display = ['abbreviated_title']



admin.site.register(LegalEntity, LegalEntity)