from django.db import models

# Create your models here.
class Resume(models.Model):
    resume_company_name = models.CharField(max_length=50)
    resume_link = models.URLField(max_length=200, default='')
    #Original Link: https://drive.google.com/file/d/1M1aaXO6yGrYTnFTuCxAwCDzofA7XJs53/view?usp=share_link
    #Download Link: https://drive.google.com/uc?export=download&id=1M1aaXO6yGrYTnFTuCxAwCDzofA7XJs53

    def __str__(self) -> str:
        return self.resume_company_name