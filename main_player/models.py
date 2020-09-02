from django.db import models

# Create your models here.
class video_model(models.Model):
    video_filename = models.CharField(max_length=200)
    video_file_extension = models.CharField(max_length=200)
    video_sub_enable = models.BooleanField(default=False)
    
