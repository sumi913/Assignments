from django.contrib import admin
from django.urls import path, include

from .views import home_view, about_view

urlpatterns = [
    path('', home_view, name="home"),
    path('about', about_view, name="about")
]
