from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Article

# Create your views here.
class ArticleView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id, published=True)

        context = { 'article': article }
        template = 'news/article.html'
        return render(request, template, context)


def article_list(request):
    articles = Article.objects.published()

    context = { 'articles': articles }
    template = 'news/list.html'
    return render(request, template, context)
