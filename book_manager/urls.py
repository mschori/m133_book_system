from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('authors', views.show_authors, name='authors'),
]
