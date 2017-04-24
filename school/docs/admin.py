from django.contrib import admin
from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    fields = ('title', 'paper', 'link', 'revised_at', 'created_at', 'updated_at', )
    readonly_fields = ('created_at', 'updated_at', )
    list_display = ('title', 'created_at', )

admin.site.register(Document, DocumentAdmin)
