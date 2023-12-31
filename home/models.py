from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    bannerImg = CloudinaryField('Banner Images')
  
    
    def __str__(self):
        return str(self.id)
    
class About_Section(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class About_Section_Images(models.Model):
    aboutImg = CloudinaryField('AboutSec Images')
  
    def __str__(self):
        return str(self.id)    

    
class Vision_and_Mission(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class Gallery_Section(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class Gallery_Images(models.Model):
    galleryImg = CloudinaryField('Gallery_Section Images')
  
    
    def __str__(self):
        return str(self.id)
    
class Campus_Image(models.Model):
    campusImg = CloudinaryField('Campus_Images')
  
    
class Feature(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    icon = CloudinaryField('Feature Icon')
   
    
    def __str__(self):
        return str(self.id)
    
class About_Content(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    
    def __str__(self):
        return str(self.id)
    
class Why_Choose_Box(models.Model):
    count = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    icon_img = CloudinaryField('Why Choose img')
  
 
    
    def __str__(self):
        return str(self.id)
    
class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    desc = models.TextField()
    testimonialImg = CloudinaryField('Testimonial Images')
  
    
    def __str__(self):
        return str(self.id)
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    blogImg = CloudinaryField('Blog Images')

    
    def __str__(self):
        return str(self.id)
    
class Home_about_Image(models.Model):
    home_about_img = CloudinaryField('Home_about_images')
    alt_text = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.id)
    
    
    

    

    
