from django.db import models

# Create your models here.
class Rescipe (models.Model):
    rescipe_name =models.CharField(max_length=100)
    rescipe_description = models.TextField()
    rescipe_image=models.ImageField(upload_to="rescipe")
    
