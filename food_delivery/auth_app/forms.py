from django import forms

from auth_app.models import User

class AuthBaseForm(forms.Form):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )

class RegistrationForm(AuthBaseForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Введите email'})
    )

    password_confirmed = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
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
    pass
