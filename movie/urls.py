from django.contrib import admin
from django.urls import path

from .views import get_page_movie

urlpatterns = [path("page/<int:n>/", get_page_movie)]
