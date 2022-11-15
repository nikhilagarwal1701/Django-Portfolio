from django.contrib import admin
from .models import Resume

# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Name', {'fields': ['resume_company_name']}),
        ('Download Link', {'fields': ['resume_link']})
    ]


admin.site.register(Resume, ResumeAdmin)