from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib import messages,auth


def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mail']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                return redirect("login")

        else:
            messages.info(request,'password not matching')
            return  redirect('register')
        return redirect('home')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
# Create your views here.
