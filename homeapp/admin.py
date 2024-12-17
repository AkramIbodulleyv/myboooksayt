from django.contrib import admin

from homeapp.forms import SotishForm

from .models import Books,foydalanuvchimalumoti,Sotish


@admin.register(Books)
class Adminbook(admin.ModelAdmin):
    list_display = ('title','pages','published_date','price','author','bio')

@admin.register(foydalanuvchimalumoti)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("username","phone","email","birth_date","job")


@admin.register(Sotish)
class SotishAdmin(admin.ModelAdmin):
    list_display = ('name','phone','location','about')
    form = SotishForm