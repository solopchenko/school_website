from django.db import models
from django.conf import settings
from .utils import get_user_profile_photo_upload_to

# Create your models here.
class Postion(models.Model):
    name = models.CharField(verbose_name="Наименование должности", max_length=200)
    is_chief = models.BooleanField(verbose_name="Администрация", default=False)

    def persons(self):
        return self.person_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Person(models.Model):
    login = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Логин")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    photo = models.FileField(verbose_name='Фотография', upload_to=get_user_profile_photo_upload_to, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    office = models.CharField(max_length=100, verbose_name='Кабинет')
    education = models.CharField(max_length=500, verbose_name='Образование', blank=True)
    teaching_experience = models.CharField(max_length=200, verbose_name='Педагогический стаж', blank=True)
    positions = models.ManyToManyField(Postion, verbose_name="Должности", blank=True)

    def full_name(self):
        if self.middle_name:
            return self.last_name + ' ' + self.first_name + ' ' + self.middle_name
        else:
            return self.last_name + ' ' + self.first_name

    def get_positions(self):
        positions = self.positions.all()
        str_positions = positions[:1]
        for position in positions[1:]:
            str_positions = str_positions + ', ' + position
        return str_positions

    def tabs(self):
        return self.persontab_set.all()

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name', 'middle_name']

class PersonTab(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Сотрудник")
    name = models.CharField(max_length=100, verbose_name="Имя вкладки")
    content = models.TextField(verbose_name="Контент вкладки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вкладка'
        verbose_name_plural = 'Вкладки'
