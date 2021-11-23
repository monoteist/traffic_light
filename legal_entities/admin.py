from django.contrib import admin
from legal_entities.models import LegalEntity

from clients.models import Client


class ClientInline(admin.TabularInline):
    model = Client

admin.site.register(LegalEntity)
