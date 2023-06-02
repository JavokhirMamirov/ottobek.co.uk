from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class HomeBarner(models.Model):
    text = RichTextField()
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text[:30]

class AboutUs(models.Model):
    title = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:30]
    
class AboutUsItem(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class FAQItem(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField('images/', null=True, blank=True)
    text = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ProjectItem(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    website_title = models.TextField()
    phone = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
 


class Footer(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

