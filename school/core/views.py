from django.shortcuts import render
from django.views import View
from .models import Organisation

# Create your views here.
class HomeView(View):
    def get(self, request):
        organisation = Organisation.objects.first()
        return render(request, 'home.html', {'organisation': organisation})
