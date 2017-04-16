from django.shortcuts import render
from django.views import View
from .models import Site
from news.models import Article

# Create your views here.
class HomeView(View):
    def get(self, request):
        page = Site.objects.all().first().homepage
        articles = Article.objects.published()

        context = { 'page': page, 'articles': articles }
        template = 'pages/home.html'
        return render(request, template, context)
