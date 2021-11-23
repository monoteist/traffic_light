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

    def save(self, *args, **kwargs):
        if not self.id:
            max = LegalEntity.objects.aggregate(id_max=models.Max('id'))['id_max']
            self.id = 101 if max is None else max * 100 + 2
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'
