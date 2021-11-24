from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'first_name', 'last_name',
                  'second_name', 'phone', 'type_of', 'is_active', 'gender', 'timezone', 'odnoklassniki', 'instagram', 'telegram', 'whatsapp', 'viber', 'legal_entity')
