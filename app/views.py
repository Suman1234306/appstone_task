from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth
# Create your views here.

def index(request):

    return render(request,'login_signup.html')

@login_required(login_url="index")
def welcome(request):
    user = User.objects.get(id=request.user.id)
    return render(request,"welcome.html",{"user":user})

def signup_action(request):
    fullname = request.POST.get("fullname")
    email = request.POST.get("email")
    password = request.POST.get("password")
    phone = request.POST.get("phone")
    type = request.POST.get("type")
    user = User.objects.create_user(email=email,password=password)
    user.fullname=fullname
    user.email=email
    user.phone=phone
    user.type=type
    user.save()
    return redirect("welcome")

def login_action(request):

    email = request.POST.get("email")
    password = request.POST.get("password")
    user = auth.authenticate(request,email=email,password=password)
    auth.login(request,user)
    return redirect("welcome")