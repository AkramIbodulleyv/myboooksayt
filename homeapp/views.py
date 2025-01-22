import cmd
import random
import smtplib
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm
from .utils import save_verification_code, send_verification_email, generate_verification_code
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from homeapp.forms import VerificationForm
from .models import AddBook, VerificationCode
from django.contrib.auth.hashers import make_password
from email.mime.text import MIMEText
from bookproject.settings import *
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .forms import UserChangeForm

@login_required(login_url='signup')
def quizgame(request):
    return render(request, 'snakegames.html')



def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            verification_code = random.randint(100000, 999999)

            request.session['verification_code'] = verification_code
            request.session['user_id'] = user.id

            send_mail(
                'Email Verification',
                f'Your verification code is: {verification_code}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return redirect('verify_email')

    else:
        form = RegistrationForm()

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
                return redirect('base')
            else:
                messages.error(request, 'Username or password is incorrect')
    return render(request, 'registration/login.html', {'form': form})

from django.views.generic import ListView
from .models import AddBook

class Asosiypanel(ListView):
    model = AddBook
    template_name = 'asosiypanel.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        genre_filter = self.request.GET.get('genre', '')

        if search_query:
            queryset = queryset.filter(
                title__icontains=search_query
            ) | queryset.filter(author__icontains=search_query)

        if genre_filter:
            queryset = queryset.filter(genre=genre_filter)

        return queryset.order_by('?')



def custom_logout(request):
    logout(request)
    messages.success(request, 'Siz muvaffaqiyatli chiqdingiz!')
    return redirect('base')



@login_required(login_url='signup')
def bookdetails(request, book_id):
    book = AddBook.objects.get(id=book_id)
    related_books = AddBook.objects.filter(genre=book.genre).exclude(id=book_id)
    return render(request, 'info.html', {'book': book, 'related_books': related_books})






def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = send_verification_email(email)

            verification, created = VerificationCode.objects.get_or_create(email=email)
            verification.code = code
            verification.save()

            request.session['email'] = email
            return redirect('verify_email')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})





def verify_email_view(request):
    if request.method == 'POST':
        input_code = request.POST.get('verification_code')
        stored_code = request.session.get('verification_code')
        user_id = request.session.get('user_id')

        if input_code and str(input_code) == str(stored_code):
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()
            del request.session['verification_code']
            del request.session['user_id']

            return redirect('login')
        else:
            return render(request, 'verify_email.html', {
                'error': 'Invalid verification code'
            })

    return render(request, 'verify_email.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Task.objects.create(name=text)
        return redirect('task_list')

    tasks = Task.objects.all()
    return render(request, '12.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def view_text(request):
    text = get_object_or_404(TextModel, id=1)
    return render(request, '12.html', {'text': text})


def finished(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = "Completed"
    task.save()
    return redirect('/12/')





@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profilingiz yangilandi')
            return redirect('base')  # Yangi profil sahifasiga yo'naltirish
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})
