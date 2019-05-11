from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView, LogoutView
)

from .forms import LoginForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class Logout(LogoutView):
    template_name = 'registration/logout.html'
