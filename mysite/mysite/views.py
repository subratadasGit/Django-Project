from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello, world. You're at about Page")

def contact(request):
    return HttpResponse("Hello, world. You're at contact Page")
