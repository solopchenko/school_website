from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Register your models here.
class UserProfileInLine(admin.StackedInline):
    model = UserProfile

class ExtendedUserAdmin(UserAdmin):
    list_display = ('userprofile', 'username', 'is_active', )
    inlines = (UserProfileInLine, )

#Приложение auth
admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    pass

#Приложение staff
admin.site.register(UserProfile, UserProfileAdmin)
