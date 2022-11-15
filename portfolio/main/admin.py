from django.contrib import admin
from datetime import datetime
from .models import Wallpaper


class WallpaperAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields": ["wallpaper_name", "wallpaper_date"]}),
        ("Image", {"fields": ["wallpaper_image"]})
    ]


# Register your models here.
admin.site.register(Wallpaper, WallpaperAdmin)