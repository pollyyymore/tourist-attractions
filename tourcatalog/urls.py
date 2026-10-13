"""Корневая конфигурация маршрутов проекта TourCatalog."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("places/", include("places.urls")),
    path("users/", include("users.urls")),
    path("favorites/", include("favorites.urls")),
]

handler404 = "homepage.views.page_not_found"