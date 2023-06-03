from django.shortcuts import render
from home.models import *
# Create your views here.
def home_view(request):
    contact = Contact.objects.filter(is_active=True).last()
    barners = HomeBarner.objects.filter(is_active=True)[0:3]
    aboutus = AboutUs.objects.filter(is_active=True).last()
    context = {
        'contact':contact,
        'barners':barners,
        'aboutus':aboutus,
    }
    return render(request, 'index.html', context=context)