from django.db import models
import django.contrib.gis
from django.core.validators import FileExtensionValidator
from django.db.models import Model
from django_resized import ResizedImageField

class AddBook(models.Model):
    GENRE_CHOICES = [
        ("Diniy", "Diniy"),
        ("Jadid Adabiyoti", "Jadid Adabiyoti"),
        ("Zamonaviy", "Zamonaviy"),
        ("Ishqiy", "Ishqiy"),
    ]
    title = models.CharField(max_length=350, verbose_name="Kitob nomi")
    pages = models.PositiveIntegerField(verbose_name="Sahifalar soni")
    year = models.DateField(verbose_name="Chop etilgan sana")
    price = models.PositiveIntegerField(verbose_name="Narxi (so'm)")
    book_image = ResizedImageField(size=[220,320],crop=['middle','center'],upload_to='image/', null=True, blank=True, verbose_name="Kitob rasmi",validators=[FileExtensionValidator(['jpg','jpeg','png','bmp','webp'])])
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, verbose_name="Janr")
    author = models.CharField(max_length=225, verbose_name="Muallif")
    isbn = models.CharField(max_length=13, verbose_name="ISBN")
    bio = models.TextField(verbose_name="Annotatsiya")

    def __str__(self):
        return self.title

class VerificationCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return (now() - self.created_at).seconds > 60




from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='In progress')

    def __str__(self):
        return self.name

class TextModel(models.Model):
    content = models.TextField()




class botsavemodel(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_type = models.CharField(max_length=50,default='text')

    def __str__(self):
        return f"{self.username or self.user_id} - {self.message[:20]}"