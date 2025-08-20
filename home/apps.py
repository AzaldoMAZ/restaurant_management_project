from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
# app.py  (you can name the app whatever you want)

from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.urls import path

# ---------------------------
# Model
# ---------------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# ---------------------------
# View
# ---------------------------
def home(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant else getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    return render(request, "home.html", {"restaurant_name": restaurant_name})

# ---------------------------
# URL patterns
# ---------------------------
urlpatterns = [
    path("", home, name="home"),
]
