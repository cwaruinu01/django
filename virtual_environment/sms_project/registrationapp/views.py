from urllib import request

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import  registration,student





def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


@csrf_exempt
def regpage(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name= request.POST.get('lname')
        date_of_birth=request.POST.get('age')
        password = request.POST.get('pass')
        email= request.POST.get('email')
        mydata={'first_name':first_name,'last_name':last_name,'email':email,'password':password,'date_of_birth':date_of_birth}
        print(mydata)

        query=registration(first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,email=email,password=password)
        query.save()

        data=registration.objects.all()
        context={'data':data}
    return render(request, 'register.html',context)


