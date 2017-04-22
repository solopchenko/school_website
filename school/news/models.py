from django.db import models
from django.conf import settings
from .managers import ArticleManager

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    announcement = models.TextField(verbose_name='Анонс', max_length=500, help_text='Отображается вверху новости. Форматирование текста <b>не поддерживается.</b>')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    published = models.BooleanField(verbose_name='Опубликовать', default=True)

    objects = ArticleManager()

    def get_absolute_url(self):
        return "/news/{0}".format(self.pk)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
