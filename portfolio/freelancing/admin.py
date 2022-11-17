
from django.contrib import admin
from datetime import datetime
from .models import Wallpaper


class WallpaperAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields": ["wallpaper_name", "wallpaper_date"]}),
        ("Google Drive URL", {"fields": ["wallpaper_drive_url"]}),
        ("Image", {"fields": ["wallpaper_image"]}),
    ]


# Register your models here.
admin.site.register(Wallpaper, WallpaperAdmin)