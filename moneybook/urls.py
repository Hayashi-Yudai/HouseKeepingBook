from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "moneybook"
urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("<int:year>/<int:month>", views.MainView.as_view(), name="index"),
]
