from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('author', 'created_at', 'updated_at', 'title', 'announcement', 'content', 'published', )
    readonly_fields = ('author', 'created_at', 'updated_at', )
    list_display = ('title', 'published', 'created_at', 'updated_at', )

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
