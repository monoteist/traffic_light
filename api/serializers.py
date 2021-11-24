from rest_framework import serializers

from clients.models import Client, Phone, Email, VK, FB


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
                  'second_name', 'phone', 'type_of', 'is_active', 'gender', 'timezone', 'odnoklassniki', 'instagram', 'telegram', 'whatsapp', 'viber', 'legal_entity', 'phones', 'emails', 'vk', 'fb')
