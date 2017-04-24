from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Document

# Create your views here.
def docs_list(request):
    documents = Document.objects.all()
    context = { 'documents': documents }
    template = 'docs/list.html'
    return render(request, template, context)
