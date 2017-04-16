
from django.contrib import admin
from .models import Page, Section

# Register your models here.

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0


class PageAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'parent', 'url', 'created_at', 'updated_at', )
    readonly_fields = ('url', 'created_at', 'updated_at', )
    list_display = ('title', 'url', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title', )}

    inlines = (SectionInline, )

    def save_model(self, request, obj, form, change):

        obj.slug = obj.slug.lower()

        if obj.parent:
            obj.url = obj.parent.url + '/' + obj.slug
        else:
            obj.url = obj.slug

        obj.save()

admin.site.register(Page, PageAdmin)
