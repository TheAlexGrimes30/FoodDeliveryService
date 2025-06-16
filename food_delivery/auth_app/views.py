from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from auth_app.forms import RegistrationForm
from auth_app.models import User


def index(request):
    return render(request, "index.html")

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        User.objects.create(
            username=form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = make_password(form.cleaned_data['password'])
        )
        return super().form_valid(form)
