from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def freelance_home(request):
    return render(request, "freelancing/freelance_home.html")