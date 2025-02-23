from django.shortcuts import render

def home(request):
    return render(request, "event/index.html") 

def RegisterPage(request):
    return render(request, "event/register.html") 

def Login(request):
    return render(request, "event/login.html") 