from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    slug = models.SlugField(verbose_name="Адрес страницы")
    url = models.CharField(verbose_name='URL', max_length=2500)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата последнего изменения", auto_now=True)

    parent = models.ForeignKey('self', verbose_name="Родительская страница", on_delete=models.PROTECT, null=True, blank=True)

    def sections(self):
        return self.section_set.all()

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
