from django.contrib import admin
from .models import Organisation, OrganisationBuilding

# Register your models here.

class OrganisationBuildingInline(admin.StackedInline):
    model = OrganisationBuilding
    extra = 0


class OrganisationAdmin(admin.ModelAdmin):
    inlines = (OrganisationBuildingInline, )

    #Ограничение на добавление объектов.
    #Не может быть более 1 объекта.
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            super().has_add_permission(request)

    #Ограничение на удаление объектов.
    #Нельзя удалить все объекты.
    def has_delete_permission(self, request, obj=None):
        if self.model.objects.count() == 1:
            return False
        else:
            super().has_delete_permission(request)

admin.site.register(Organisation, OrganisationAdmin)
