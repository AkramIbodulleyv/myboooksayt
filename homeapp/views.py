import cmd
import smtplib

from django.conf.global_settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST_PASSWORD
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from homeapp.forms import RegistrationForm
from .models import AddBook
from django.contrib.auth.hashers import make_password
from email.mime.text import MIMEText
from bookproject.settings import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string

def snakegame(request):
    return render(request, 'snakegames.html')



def signup_view(request):
    form = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.is_active = False
            form.save()
            return redirect('base/')
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    form = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('/base/')
            else:
                messages.error(request, 'Username or password is incorrect')
    return render(request, 'registration/login.html', {'form': form})


class Asosiypanel(ListView):
    model = AddBook
    template_name = 'asosiypanel.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        genre_filter = self.request.GET.get('genre', '')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(author__icontains=search_query)

        if genre_filter:
            queryset = queryset.filter(genre=genre_filter)

        return queryset



def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        pages = request.POST.get("pages")
        year = request.POST.get("year")
        price = request.POST.get("price")
        genre = request.POST.get("genre")
        author = request.POST.get("author")
        bio = request.POST.get("bio")
        isbn = request.POST.get("isbn")
        book_image = request.FILES.get("book_image")

        new_book = AddBook(title=title, pages=pages, year=year,
                           price=price, genre=genre, author=author,
                           bio=bio, isbn=isbn, book_image=book_image)

        new_book.save()

        return redirect('/base/')

    return render(request,'addbook.html')



def bookdetails(request, book_id):
    book = AddBook.objects.get(id=book_id)
    related_books = AddBook.objects.filter(genre=book.genre).exclude(id=book_id)  # Example filter for related books
    return render(request, 'info.html', {'book': book, 'related_books': related_books})