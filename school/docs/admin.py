from django.contrib import admin
from .models import Document, Category

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    fields = ('title', 'paper', 'link', 'revised_at', 'category', 'created_at', 'updated_at', )
    readonly_fields = ('created_at', 'updated_at', )
    list_display = ('title', 'category', 'created_at', )
    list_filter = ('category', 'category__is_public', )

admin.site.register(Document, DocumentAdmin)
admin.site.register(Category)
