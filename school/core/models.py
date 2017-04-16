from django.db import models
from pages.models import Page

# Create your models here.

class Site(models.Model):
    title = models.CharField(verbose_name="Заголовок сайта", max_length=200)
    description = models.CharField(verbose_name="Описание сайта", max_length=500, blank=True)
    homepage = models.OneToOneField(Page, verbose_name="Главная страница")

    def name(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'



class Organisation(models.Model):
    full_name = models.CharField(verbose_name="Полное наименование", max_length=500)
    short_name = models.CharField(verbose_name="Сокращенное наименование", max_length=200, blank=True)
    email = models.EmailField(verbose_name="Электронная почта", blank=True)
    website = models.URLField(verbose_name="Сайт")

    def name(self):
        if self.short_name:
            return self.short_name
        else:
            return self.full_name

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Информация об организации'
        verbose_name_plural = 'Информация об организации'

class OrganisationBuilding(models.Model):
    name = models.CharField(verbose_name="Наименование здания", max_length=200)
    address = models.CharField(verbose_name="Адрес", max_length=500)
    phone = models.CharField(verbose_name="Телефон", max_length=25)
    business_hours = models.TextField(verbose_name='Часы работы', max_length=500)
    visiting_hours = models.TextField(verbose_name='Часы приема', max_length=500, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
