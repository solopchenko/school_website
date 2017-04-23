from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Page

# Create your views here.
def pages_detail(request, page_url):
    page = get_object_or_404(Page.objects.published(), url=page_url)
    context = { 'page': page }
    template = 'pages/page.html'
    return render(request, template, context)
