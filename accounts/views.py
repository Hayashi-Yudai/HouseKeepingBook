from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import (
    LoginView, LogoutView
)

from .forms import LoginForm, SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class Logout(LogoutView):
    template_name = 'registration/logout.html'
