from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('author', 'created_at', 'updated_at', 'published_at', 'is_published', 'title', 'announcement', 'content', )
    readonly_fields = ('author', 'created_at', 'updated_at', 'published_at', )
    list_display = ('title', 'is_published', 'published_at', 'created_at')
    list_filter = ('is_published', 'published_at', 'author__person', )

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'author'):
            obj.author = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Article, ArticleAdmin)
