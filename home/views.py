from django.shortcuts import render, redirect
from home.models import *
# Create your views here.
def home_view(request):
    contact = Contact.objects.filter(is_active=True).last()
    barners = HomeBarner.objects.filter(is_active=True)
    aboutus = AboutUs.objects.filter(is_active=True).last()
    aboutus_items = AboutUsItem.objects.filter(is_active=True)
    faq = FAQ.objects.filter(is_active=True).last()
    faq_items = FAQItem.objects.filter(is_active=True)[:3]
    services = Service.objects.filter(is_active=True)
    project = Project.objects.filter(is_active=True).last()
    project_items = ProjectItem.objects.filter(is_active=True)
    footer = Footer.objects.filter(is_active=True)
    if footer.count() == 0:
        col = 0
    elif footer.count() == 1:
        col = 12
    elif footer.count() == 2:
        col = 6
    elif footer.count() == 3:
        col = 4
    else:
        col = 3
    
    context = {
        'contact':contact,
        'barners':barners,
        'aboutus':aboutus,
        'aboutus_items':aboutus_items,
        'faq':faq,
        'faq_items':faq_items,
        'services':services,
        'project':project,
        'project_items':project_items,
        'footer':footer,
        'col':col
    }
    return render(request, 'index.html', context=context)


def send_message_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Message.objects.create(first_name=first_name, email=email, phone=phone, message=message)

        return redirect('home')
    return redirect('home')