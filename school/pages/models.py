from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver

from .utils import get_slide_upload_to

# Create your models here.
class Page(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    slug = models.SlugField(verbose_name="Адрес страницы")
    url = models.CharField(verbose_name='URL', max_length=2500)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата последнего изменения", auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовать', default=True)

    parent = models.ForeignKey('self', verbose_name="Родительская страница", on_delete=models.PROTECT, null=True, blank=True)

    def sections(self):
        return self.section_set.all()

    def slider(self):
        return self.slide_set.all()

    def parents(self):
        pages = []
        pg = self
        while pg.parent:
            pg = pg.parent
            pages.append(pg)
        return pages

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        unique_together = ('parent', 'slug')

class Section(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    show_title = models.BooleanField(verbose_name='Отображать заголовок', help_text='Обычно загловок элемента отображают на странице', default=True)
    anchor = models.SlugField(verbose_name="Якорная ссылка", help_text='Задаёт уникальный идентификатор элемента на странице', blank=True)
    content = models.TextField(verbose_name="Контент", help_text='Поле может содержать HTML-тэги', blank=False)
    full_width = models.BooleanField(verbose_name='Секция во всю ширину', help_text='Обычно используется для слайдеров и карт', default=False)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="Страница")

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = 'Элемент страницы'
            verbose_name_plural = 'Элементы страницы'

class Slide(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="Страница")
    background_image = models.FileField(verbose_name="Фоновое изображение", upload_to=get_slide_upload_to)
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    subtitle = models.CharField(verbose_name="Подзаголовок", max_length=500, blank=True)
    link = models.URLField(verbose_name='Ссылка на страницу', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Слайдер'

#Автоматическое удаление изображения слайдера при удалении слайда
@receiver(post_delete, sender=Slide)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.background_image:
        instance.background_image.delete(save=False)

#Автоматическое удаление старого изображения слайдера при изменении слайда
@receiver(pre_save, sender=Slide)
def auto_delte_file_on_change(sender, instance, **kwargs):
    #Если изменяем модель
    if instance.pk:
        old_instance = Slide.objects.get(pk=instance.pk)
        old_background_image = old_instance.background_image if old_instance.background_image else None
        new_background_image = instance.background_image

        if not old_background_image == new_background_image:
            old_background_image.delete(save=False)
