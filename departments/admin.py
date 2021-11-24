from django.contrib import admin

from departments.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    def client_count(self):
        return 1
    client_count.short_description = 'Количество клиентов'
    fields = ('title', 'legal_entity', 'client')
    list_display = ('title', 'legal_entity', 'client_count')


admin.site.register(Department, DepartmentAdmin)