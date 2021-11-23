from django.db import models


class LegalEntity(models.Model):
    full_title = models.CharField(
        max_length=250, verbose_name='Название полное')
    abbreviated_title = models.CharField(
        max_length=50, verbose_name='Название сокращенное')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    inn = models.CharField(max_length=10, verbose_name='ИНН')
    kpp = models.CharField(max_length=10, verbose_name='КПП')

    def __str__(self) -> str:
        return self.full_title
    

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'
