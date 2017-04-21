from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('author', 'created_at', 'updated_at', 'title', 'announcement', 'content', 'published', )
    readonly_fields = ('author', 'created_at', 'updated_at', )
    list_display = ('title', 'published', 'created_at', 'updated_at', )

admin.site.register(Article, ArticleAdmin)
