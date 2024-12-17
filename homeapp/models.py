from django.db import models
import django.contrib.gis
# Create your models here.

class foydalanuvchimalumoti(models.Model):
    objects = None
    username = models.CharField(max_length=225)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Books(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    images = models.ImageField(upload_to='image/', null = True,blank=True)
    published_date = models.DateField()
    price = models.IntegerField()
    author = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Sotish(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Books, null=True, blank=True,on_delete=models.SET_NULL)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    about = models.CharField(max_length=200)


    def __str__(self):
        return self.name