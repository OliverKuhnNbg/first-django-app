from django.shortcuts import render
from django.http import HttpResponse;

def hello_world_view(request):
    return HttpResponse("Hello World")

def hello_py_view(request):
    return HttpResponse("Hello Pyton - Start Page")

