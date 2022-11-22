from django.db import models

# Create your models here.
class Resume(models.Model):
    resume_company_name = models.CharField(max_length=50)
    resume_link = models.URLField(max_length=200, default='')


    def __str__(self) -> str:
        return self.resume_company_name