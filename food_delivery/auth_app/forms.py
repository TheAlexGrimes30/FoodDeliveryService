from django import forms
from django.contrib.auth import authenticate

from auth_app.models import User

class AuthBaseForm(forms.Form):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин', 'class': 'form-control'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'})
    )

class RegistrationForm(AuthBaseForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Введите email', 'class': 'form-control'})
    )

    password_confirmed = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с таким {username} уже существует')
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Пользователь с таким {email} уже существует')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmed_password = cleaned_data.get("password_confirmed")

        if password and confirmed_password and password != confirmed_password:
            raise forms.ValidationError("Пароли не совпадают")

        if password and len(password) < 8:
            self.add_error('password', "Пароль слишком короткий (минимум 8 символов)")

class AuthForm(AuthBaseForm):

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Неверный логин или пароль")

        return cleaned_data

