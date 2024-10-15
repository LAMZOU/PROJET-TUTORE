
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def collect(request):
    return render(request,'collect/collect.html')