from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    # context = {                                          #context = set of variables to be sent
    #     'variable':"This is sent"
    # }
    return  render(request, 'index.html')
    # return HttpResponse('This is Homepage')     #HttpResponse() renders a string on a webpage..practically we dont use this.

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is Aboutpage')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is servicespage')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,phone=phone, desc=desc,date= datetime.today())
        contact.save()

    return render(request, 'contact.html')

    # return HttpResponse('This is Contactpage')