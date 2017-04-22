from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Person, PersonTab

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

class PersonTabInline(admin.StackedInline):
    model = PersonTab
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    #inlines = (UserInLine, )
    list_display = ('full_name', 'login', 'office', )
    list_filter = ('login__is_active', 'login__is_superuser', )
    filter_horizontal = ('positions', )
    inlines = (PersonTabInline, )
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
