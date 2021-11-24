from django.db import models


class Department(models.Model):
    id = models.IntegerField(unique=True)
    custom_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Название')
    legal_entity = models.ForeignKey(
        'legal_entities.LegalEntity', on_delete=models.SET_NULL, null=True, verbose_name='Юридическое лицо')
    client = models.ForeignKey(
        'clients.Client', on_delete=models.SET_NULL, null=True, verbose_name='Клиент')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            max = Department.objects.aggregate(id_max=models.Max('custom_id'))['id_max']
            self.id = 103 if max is None else (max + 1) * 100 + 3
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
