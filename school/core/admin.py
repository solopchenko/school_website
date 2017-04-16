from django.contrib import admin
from .models import Organisation, OrganisationBuilding, Site

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    pass
    #Ограничение на добавление объектов.
    #Не может быть более 1 объекта.
    #def has_add_permission(self, request):
    #    if self.model.objects.count() > 0:
    #        return False
    #    else:
    #        super(SiteAdmin, self).has_add_permission(request)

    #Ограничение на удаление объектов.
    #Нельзя удалить все объекты.
    #def has_delete_permission(self, request, obj=None):
    #    if self.model.objects.count() == 1:
    #        return False
    #    else:
    #        super(SiteAdmin, self).has_delete_permission(request)

admin.site.register(Site, SiteAdmin)


class OrganisationBuildingInline(admin.StackedInline):
    model = OrganisationBuilding
    extra = 0


class OrganisationAdmin(admin.ModelAdmin):
    inlines = (OrganisationBuildingInline, )

    #Ограничение на добавление объектов.
    #Не может быть более 1 объекта.
    #def has_add_permission(self, request):
    #    if self.model.objects.count() > 0:
    #        return False
    #    else:
    #        super(OrganisationAdmin, self).has_add_permission(request)

    #Ограничение на удаление объектов.
    #Нельзя удалить все объекты.
    #def has_delete_permission(self, request, obj=None):
    #    if self.model.objects.count() == 1:
    #        return False
    #    else:
    #        super(OrganisationAdmin, self).has_delete_permission(request)

admin.site.register(Organisation, OrganisationAdmin)
