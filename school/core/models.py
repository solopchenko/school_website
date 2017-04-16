from django.db import models

# Create your models here.
class Site(models.Model):
    title = models.CharField(verbose_name='Полное наименование', max_length=200)
    description = models.CharField(verbose_name='Полное наименование', max_length=500, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
