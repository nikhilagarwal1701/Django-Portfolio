from django.shortcuts import render
from django.http import HttpResponse
from .models import Wallpaper
# Create your views here.

def freelance_home(request):
    return render(request, "freelancing/freelance_home.html")

def wallpaper_thumbnail(request):
    return render(request, 'freelancing/wallpaper_thumbnail.html', {"wallpapers": Wallpaper.objects.all})

def video_edits(request):
    return render(request, 'freelancing/video_edits.html')