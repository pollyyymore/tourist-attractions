"""Маршруты приложения favorites."""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.favorites, name="favorites"),
    path("<int:favorite_id>/", views.favorite_detail, name="favorite_detail"),
]