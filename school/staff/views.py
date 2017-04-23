from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Person

# Create your views here.
def staff_list(request):
    return render(request, 'staff/list.html', {})

def staff_detail(request, username):
    person = get_object_or_404(Person, login__username=username)
    context = { 'person': person }
    template = 'staff/detail.html'
    return render(request, template, context)
