
from django.contrib import admin
from .models import Page, Section, Slide

# Register your models here.

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0

class SlideInLine(admin.TabularInline):
    model = Slide
    fields = ('title', 'subtitle', 'link', 'background_image', )
    extra = 0


class PageAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'slug', 'parent', 'url', 'created_at', 'updated_at', )
    readonly_fields = ('author', 'url', 'created_at', 'updated_at', )
    list_display = ('title', 'url', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title', )}

    inlines = (SectionInline, SlideInLine)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'author'):
            obj.author = request.user

        obj.slug = obj.slug.lower()
        if obj.parent:
            obj.url = obj.parent.url + '/' + obj.slug
        else:
            obj.url = obj.slug
        obj.save()

admin.site.register(Page, PageAdmin)
