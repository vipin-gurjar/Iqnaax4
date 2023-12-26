from django.db import models
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

# Create your models here.    
class We_Different(models.Model):
    title = models.CharField(max_length=200)
    different_Img = models.ImageField(upload_to='Different_Images')
    
    def __str__(self):
        return str(self.id)


class About_Area_Content(models.Model):
    content = HTMLField()
    
class About_image_gallery(models.Model):
    about_img_gallery = CloudinaryField('About_image_gallery')
    
    def __str__(self):
        return str(self.id)
    
class Reason_to_shop(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    medalImg = models.ImageField(upload_to='Medal Images')
    
    def __str__(self):
        return str(self.id)
    
class Counterup_content(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
    
