from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article

# Create your views here.
def news_detail(request, article_id):
    article = get_object_or_404(Article.objects.published(), pk=article_id)
    context = { 'article': article }
    template = 'news/article.html'
    return render(request, template, context)

def news_list(request):
    articles = Article.objects.published()
    context = { 'articles': articles }
    template = 'news/list.html'
    return render(request, template, context)
