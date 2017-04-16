from django.shortcuts import render
from django.views import View
from .models import Site

# Create your views here.
class HomeView(View):
    def get(self, request):
        page = Site.objects.all().first().homepage

        context = {'page': page}
        template = 'page.html'
        return render(request, template, context)
