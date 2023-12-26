from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Gallery_Images(models.Model):
    images = CloudinaryField('Gallery Images')
    
   
