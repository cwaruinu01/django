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
    if request.method=='post':
        first_name=request.post.get('fname')
        last_name= request.post.get('lname')
        date_of_birth=request.post.get('age')
        password = request.post.get('pass')
        email= request.post.get('email')
        mydata={'first_name':first_name,'last_name':last_name,'email':email,'password':password,'date_of_birth':date_of_birth}
        print(mydata)

        query=registration(first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,email=email,password=password)
        query.save()
    return render(request, 'home.html')
