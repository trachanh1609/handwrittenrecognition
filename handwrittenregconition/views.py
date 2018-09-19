from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import platform

def index(request):
    return HttpResponse("Hello world ! Python version is " + platform.python_version() + ".")