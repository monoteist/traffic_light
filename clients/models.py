
import pytz
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    TYPE_CHOICES = (
        ('PRIMARY', 'primary'),
        ('REPEATED', 'repeated'),
        ('EXTERNAL', 'external'),
        ('INDIRECT', 'indirect'),)

    GENDER_CHOICES = (
        ('МУЖСКОЙ', 'мужской'),
        ('ЖЕНСКИЙ', 'женский'),
        ('НЕИЗВЕСТНО', 'неизвестно'),
    )

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone = PhoneNumberField(unique=True, null=False,
                             blank=False, verbose_name='Телефон')
    second_name = models.CharField(
        max_length=150, blank=True, verbose_name='Отчество')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_of = models.CharField(max_length=8,
                               choices=TYPE_CHOICES, verbose_name='Тип')
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES, verbose_name='Пол')
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC', verbose_name='Часовой пояс')
    odnoklassniki = models.URLField(unique=True, verbose_name='ОК')
    instagram = models.CharField(max_length=30, unique=True)
    telegram = models.CharField(max_length=30, unique=True)
    whatsapp = PhoneNumberField(unique=True, null=False, blank=False)
    viber = PhoneNumberField(unique=True, null=False, blank=False)
    legal_entity = models.ForeignKey(
        'legal_entities.LegalEntity', on_delete=models.SET_NULL, null=True, verbose_name='Юридическое лицо')

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            max = Client.objects.aggregate(id_max=models.Max('id'))['id_max']
            self.id = 101 if max is None else max * 100 + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Phone(models.Model):
    phone = PhoneNumberField(unique=True, null=False,
                             blank=False, verbose_name='Телефон')
    client = models.ForeignKey(
        'Client', on_delete=models.CASCADE, related_name='phones')

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Email(models.Model):
    email = models.EmailField()
    client = models.ForeignKey(
        'Client', on_delete=models.CASCADE, related_name='emails')

    def __str__(self) -> str:
        return self.email


class VK(models.Model):
    vk = models.URLField()
    client = models.ForeignKey(
        'Client', on_delete=models.CASCADE, related_name='vk')

    def __str__(self) -> str:
        return self.vk


class FB(models.Model):
    fb = models.URLField()
    client = models.ForeignKey(
        'Client', on_delete=models.CASCADE, related_name='fb')

    def __str__(self) -> str:
        return self.fb
