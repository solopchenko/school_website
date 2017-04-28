from django.db import models
from django.core.exceptions import ValidationError
from .choices import MENU_POSITION_CHOICES, TOP_MENU_POSITION
from .managers import MenuManager
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


class Menu(models.Model):
    name = models.CharField(verbose_name='Название меню', max_length=200)
    link = models.URLField(verbose_name='Ссылка', blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', blank=True, null=True)
    position = models.CharField(verbose_name='Расположение', max_length=500, choices=MENU_POSITION_CHOICES, default=TOP_MENU_POSITION)

    objects = MenuManager()

    def items(self):
        return self.menuitem_set.all()

    #Дополнительная валидация модели
    def clean(self):
        #Проверка заполнения либо link, либо page, либо ничего
        if (self.link and self.page):
            raise ValidationError({
                'link': ValidationError('Выберите страницу или укажите ссылку на внешний ресурс'),
                'page': ValidationError('Выберите страницу или укажите ссылку на внешний ресурс'),
            })

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    title = models.CharField(verbose_name='Название', max_length=200)
    link = models.URLField(verbose_name='Ссылка', blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', blank=True, null=True)

    #Дополнительная валидация модели
    def clean(self):
        #Проверка обязательного заполнения либо link, либо page
        if (not self.link and not self.page) or (self.link and self.page):
            raise ValidationError({
                'link': ValidationError('Выберите страницу или укажите ссылку на внешний ресурс'),
                'page': ValidationError('Выберите страницу или укажите ссылку на внешний ресурс'),
            })

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка в меню'
        verbose_name_plural = 'Ссылки в меню'
