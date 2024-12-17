from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


from .models import Books

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


# forms.py
from django import forms

class RegistrationForm(UserCreationForm):
        first_name = forms.CharField(required=True)
        email = forms.EmailField(required=True)

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already registered')
            return email

        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'email']



from django import forms
from .models import Sotish

class SotishForm(forms.ModelForm):
    class Meta:
        model = Sotish
        fields = ['name', 'phone', 'location', 'about']
