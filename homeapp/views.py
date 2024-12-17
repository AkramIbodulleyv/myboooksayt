import cmd
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from homeapp.forms import BookForm, RegistrationForm
from homeapp.models import Books, Sotish, foydalanuvchimalumoti
from django.contrib.auth.hashers import make_password

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm



def addbook(request):
    if cmd == 'create':
            return redirect('create')
    if request.method == 'GET':
        form = BookForm()
        context = {'form': form}
        return render(request, 'addbook.html',context)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewaddbook')
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'addbook.html', context)
    
def viewaddbook(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'viewaddbook.html', context)


def deletebook(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        book.delete()
        return redirect('/bookview/')  
    except Books.DoesNotExist:
        return redirect('bookview/')
    

def editbook(request: WSGIRequest, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('viewaddbook')
        else:
            print(form.errors) 
    else:
        form = BookForm(instance=book)  
    
    context = {'form': form, 'book': book}
    return render(request, 'editbook.html', context)



from django.shortcuts import render, redirect
from .forms import SotishForm

def sotish_form(request, pk):
    book = Books.objects.get(pk=pk)  # `pk` orqali kitobni olib kelish
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SotishForm(request.POST)
            if form.is_valid():
                sotish = form.save(commit=False)
                sotish.book = book  # Sotish ma'lumotiga kitobni bog'lash
                sotish.save()
                return redirect('viewaddbook')  # Muvaffaqiyatli saqlashdan so'ng kerakli sahifaga yo'naltirish
        else:
            form = SotishForm()

        return render(request, 'sotish.html', {'form': form, 'book': book})
    else:
        return render(request, 'sotish.html', {
            'message': 'Siz tizimga kirgan emassiz. Iltimos, ro‘yxatdan o‘ting yoki tizimga kiring.'
        })



def ariza(request):
    arizalar = Sotish.objects.select_related('book').all()  # Bog'liq ma'lumotlarni optimallashtirish
    return render(request, 'viewariza.html', {'arizalar': arizalar})

def book_details(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    return render(request, 'book_details.html', {'book': book})

def signup_view(request):
    form = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.is_active = False
            form.save()
            return redirect('bookview/')
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
                return redirect('/bookview/')
            else:
                messages.error(request, 'Username or password is incorrect')
    return render(request, 'registration/login.html', {'form': form})

