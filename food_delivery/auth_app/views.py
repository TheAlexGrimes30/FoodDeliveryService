from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from auth_app.forms import RegistrationForm, AuthForm
from auth_app.models import User


def index(request):
    return render(request, "index.html")

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            is_restaurant_owner=form.cleaned_data.get('is_restaurant_owner', False)
        )
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    form_class = AuthForm
    template_name = "login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        print("form_valid reached")
        print(form.cleaned_data)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        print("Authenticated user:", user)

        if user is not None:
            login(self.request, user)
            print("Login successful:", user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Неверный логин или пароль")
            return self.form_invalid(form)

    def form_invalid(self, form):
        print("form_invalid reached")
        print("Errors:", form.errors)
        return super().form_invalid(form)

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect(reverse_lazy("index"))
