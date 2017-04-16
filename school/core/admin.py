from django.contrib import admin
from .models import Site

# Register your models here.
class SiteAdmin(admin.ModelAdmin):

    #Скрывает кнопку добавления нового элемента, если хотя бы один элемент уже есть
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return super(SiteAdmin, self).has_add_permission(request)

    #Скрывает кнопку удаления последнего, если оставлся 1 элемент
    def has_delete_permission(self, request, obj=None):
        if self.model.objects.count() < 2:
            return False
        return super(SiteAdmin, self).has_delete_permission(request)

admin.site.register(Site, SiteAdmin)
