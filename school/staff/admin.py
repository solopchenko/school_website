from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Person

# Register your models here.
class PersonInLine(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'Сотрудник'

class UserAdmin(BaseUserAdmin):
    inlines = (PersonInLine, )
    list_display = ('username', 'person', 'is_active', )

#Приложение auth
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#class UserInLine(admin.StackedInline):
#     model = settings.AUTH_USER_MODEL

class PersonAdmin(admin.ModelAdmin):
    #inlines = (UserInLine, )
    list_display = ('full_name', 'login', 'office', )
    fieldsets = (
        (None,
            {'fields': ('login', 'positions', )}
        ),
        ('Личная информация',
            {'fields': ('last_name', 'first_name', 'middle_name', 'education', 'teaching_experience', )}
        ),
        ('Контактная информация',
            {'fields': ('office', 'email', 'phone',)}
        ),
    )

#Приложение staff
admin.site.register(Person, PersonAdmin)
