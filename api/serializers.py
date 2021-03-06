from rest_framework import serializers

from clients.models import Client, Phone, Email, VK, FB
from departments.models import Department
from legal_entities.models import LegalEntity


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone',)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('email',)


class VKSerializer(serializers.ModelSerializer):
    class Meta:
        model = VK
        fields = ('vk',)


class FBSerializer(serializers.ModelSerializer):
    class Meta:
        model = FB
        fields = ('fb',)


class ClientSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    vk = VKSerializer(many=True, read_only=True)
    fb = FBSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'username', 'first_name', 'last_name',
                  'second_name', 'phone', 'type_of', 'is_active', 'gender', 'timezone', 'created_at', 'updated_at', 'odnoklassniki', 'instagram', 'telegram', 'whatsapp', 'viber', 'legal_entity', 'phones', 'emails', 'vk', 'fb')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'title', 'legal_entity', 'client')


class LegalEntitySerializer(serializers.ModelSerializer):
    clients = ClientSerializer(source='client_set', many=True)
    departments = DepartmentSerializer(source='department_set', many=True)
    class Meta:
        model = LegalEntity
        fields = ('id', 'full_title', 'abbreviated_title',
                  'created_at', 'updated_at', 'inn', 'kpp', 'clients', 'departments')
