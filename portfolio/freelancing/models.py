from django.db import models
from datetime import datetime

# Create your models here.

class Wallpaper(models.Model):
    wallpaper_name = models.CharField(max_length=30)
    wallpaper_image = models.ImageField(upload_to='main/wallpapers', default= 'wallpaper')
    wallpaper_drive_url = models.URLField(default="")
    #Original URL: https://drive.google.com/file/d/0B6wwyazyzml-OGQ3VUo0Z2thdmc/view
    #Use URL: https://drive.google.com/uc?export=view&id=0B6wwyazyzml-OGQ3VUo0Z2thdmc
    wallpaper_date = models.DateTimeField("Date Published")


    def __str__(self):
        return self.wallpaper_name
