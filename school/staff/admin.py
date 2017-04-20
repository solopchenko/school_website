from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

# Register your models here.
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Сотрудник'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInLine, )
    list_display = ('username', 'userprofile', 'is_active', )

#Приложение auth
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
