
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_recyclage(request):
    return render(request,'recyclage/list_recyclage.html')