from django.shortcuts import render
from django.views import View
from .models import Site

# Create your views here.
class HomeView(View):
    def get(self, request):
        page = Site.objects.first().homepage

        template = 'page.html'
        context = {'page': page}
        return render(request, template, context)
