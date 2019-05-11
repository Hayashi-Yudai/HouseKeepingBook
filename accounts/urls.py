from django.urls import path

from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'accounts'

urlpatterns = [
    # ex: /accounts/signup/
    path('', views.Login.as_view(), name='login'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.Logout.as_view(), name='logout')
]
