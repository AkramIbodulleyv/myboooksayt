from django.contrib import admin
from .models import AddBook


@admin.register(AddBook)
class Adminbook(admin.ModelAdmin):
    pass
