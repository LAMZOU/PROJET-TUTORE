
# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'signalement/accueil.html')