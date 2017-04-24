from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save, post_save
from django.core.exceptions import ValidationError
from .managers import CategoryManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200)
    is_public = models.BooleanField(verbose_name='Отображать на странице документов', default=False)
    description = models.TextField(verbose_name='Описание', blank=True)

    objects = CategoryManager()

    def documents(self):
        return self.document_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория документа'
        verbose_name_plural = 'Категория документов'


class Document(models.Model):
    title = models.CharField(verbose_name='Название документа', max_length=500)
    link = models.URLField(verbose_name='Ссылка на документ', blank=True)
    paper = models.FileField(verbose_name='Файл', upload_to='docs/', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата загрузки', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    revised_at = models.DateField(verbose_name='Дата последней редакции', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", blank=True, null=True)

    def __str__(self):
        return self.title

    #Дополнительная валидация модели
    def clean(self):
        #Проверка обязательного заполнения либо link, либо paper
        if (not self.link and not self.paper) or (self.link and self.paper):
            raise ValidationError({
                'link': ValidationError('Загрузите файл или укажите ссылку на документ'),
                'paper': ValidationError('Загрузите файл или укажите ссылку на документ'),
            })

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

#Автоматическое удаление файла при удалении документа
@receiver(post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.paper:
        instance.paper.delete(save=False)

#Автоматическое удаление старого файла при изменении документа
@receiver(pre_save, sender=Document)
def auto_delte_file_on_change(sender, instance, **kwargs):
    #Если изменяем модель
    if instance.pk:
        old_instance = Document.objects.get(pk=instance.pk)
        old_paper = old_instance.paper if old_instance.paper else None
        new_paper = instance.paper

        if not old_paper == new_paper and old_paper is not None:
            old_paper.delete(save=False)
