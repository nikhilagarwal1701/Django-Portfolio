from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, "software/homepage.html")

def resume(request):
    return render(request, 'software/resume.html')