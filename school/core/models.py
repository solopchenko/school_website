from django.db import models
from pages.models import Page

# Create your models here.
class Site(models.Model):
    title = models.CharField(verbose_name='Заголовок сайта', max_length=200)
    description = models.CharField(verbose_name='Описание сайта', max_length=500, blank=True)
    homepage = models.OneToOneField(Page, verbose_name="Главная страница")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
