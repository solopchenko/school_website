from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        template = 'base.html'
        context = {}
        return render(request, template, context)
