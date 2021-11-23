from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    legal_entity = models.ForeignKey(
        'legal_entities.LegalEntity', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(
        'clients.Client', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            max = Department.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            print(max)
            self.id = 101 if max is None else max * 100 + 3
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
