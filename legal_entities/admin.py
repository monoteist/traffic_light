from django.contrib import admin
from legal_entities.models import LegalEntity

class LegalEntityAdmin(admin.ModelAdmin):
    fields = ('full_title', 'abbreviated_title', 'inn', 'kpp')


admin.site.register(LegalEntity, LegalEntityAdmin)
