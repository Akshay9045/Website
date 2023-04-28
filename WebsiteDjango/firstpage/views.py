from django.shortcuts import HttpResponse,render
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("app start hui chalna")
