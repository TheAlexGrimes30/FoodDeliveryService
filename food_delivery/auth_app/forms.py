from django import forms

from auth_app.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Введите email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
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
