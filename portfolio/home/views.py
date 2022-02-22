from django.shortcuts import render, HttpResponse
from home.models import Contact 
# Create your views here.

def home(request):
    # return HttpResponse(" This is my homepage (/)")
    context = {'Name' : 'Aman', 'Course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse(" This is my about page (/)")
    return render(request, 'about.html')


def project(request):
    # return HttpResponse(" This is my project page (/)")
    return render(request, 'project.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name)
        # print(email)
        # print(phone)
        # print(desc)
        # print(name, email, phone, desc)
        # print("This is a postPOST
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
        print("The data has been written to the DATA BASE")

    # return HttpResponse(" This is my contact page (/)")
    return render(request, 'contact.html')