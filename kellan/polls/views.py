from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'polls/home.html')

def contact(request):
    return HttpResponse("About")