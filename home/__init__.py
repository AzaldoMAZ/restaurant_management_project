from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.urls import path

# ---------------------------
# Model
# ---------------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="restaurant_images/", blank=True, null=True)

    def __str__(self):
        return self.name

# ---------------------------
# Views
# ---------------------------
def home(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant else getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    return render(request, "home.html", {"restaurant_name": restaurant_name})

def about(request):
    restaurant = Restaurant.objects.first()
    return render(request, "about.html", {"restaurant": restaurant})

# ---------------------------
# URL patterns
# ---------------------------
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),