from django.contrib import admin
from django.db.models import fields
from clients.models import Client, Email, Phone, VK, FB


class EmailInline(admin.TabularInline):
    model = Email


class PhoneInline(admin.TabularInline):
    model = Phone


class VKInline(admin.TabularInline):
    model = VK


class FBInline(admin.TabularInline):
    model = FB


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        EmailInline,
        PhoneInline,
        VKInline,
        FBInline,
    ]
    fields = ['username', 'first_name', 'last_name',
              'second_name', 'phone', 'type_of', 'is_active', 'gender', 'timezone', 'odnoklassniki', 'instagram', 'telegram', 'whatsapp', 'viber']
    list_display = ['username', 'first_name', 'last_name']


admin.site.register(Client, ClientAdmin)
