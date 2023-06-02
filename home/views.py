from django.shortcuts import render
from home.models import *
# Create your views here.
def home_view(request):
    contact = Contact.objects.filter(is_active=True).last()
    context = {
        'contact':contact
    }
    return render(request, 'index.html', context=context)