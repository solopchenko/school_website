from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'announcement', 'content', 'published', 'created_at', 'updated_at', )
    readonly_fields = ('created_at', 'updated_at', )
    list_display = ('title', 'published', 'created_at', 'updated_at', )

admin.site.register(Article, ArticleAdmin)
