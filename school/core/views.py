from django.shortcuts import render
from django.views import View
from .models import Organisation

# Create your views here.
class HomeView(View):
    def get(self, request):
        page = Organisation.objects.first().main_page

        template = 'page.html'
        context = {'page': page}
        return render(request, template, context)
