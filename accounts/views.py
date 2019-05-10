from .forms import LoginForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = LoginForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
