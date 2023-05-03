from django.shortcuts import render
from .models import Place,Person
from django.http import HttpResponse
# Create your views here.

def index(request):
    obj=Place.objects.all()
    obj1=Person.objects.all()
    return render(request,'index.html',{'value':obj,'person':obj1})

def home(request):
    return render(request,'home.html')
def contact(request):
    contact_name="Balakrishnan Nair"
    return render(request,'contact.html',{'name':contact_name})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,'result.html',{'result':res})