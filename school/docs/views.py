from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category

# Create your views here.
def docs_list(request):
    document_categories = Category.objects.public()
    context = { 'document_categories': document_categories }
    template = 'docs/list.html'
    return render(request, template, context)
