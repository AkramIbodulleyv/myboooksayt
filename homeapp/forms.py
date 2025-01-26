from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('This email is already registered with another account.')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


from django import forms
from django.contrib.auth.models import User


class UserChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Username already taken')
        return username

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']



class VerificationForm(forms.Form):
    email = forms.EmailField()
    code = forms.CharField(max_length=5)