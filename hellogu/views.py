from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,"hellogu/index.html")

def sidharth(request):
    return HttpResponse("Hello Sidharth")

def shivanshu(request):
    return HttpResponse("Hello Shinu")

def greet(request, name):
    return render(request,"hellogu/index.html",{
        "name":name.capitalize()
    })