from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=255, blank=False)
    ingredients = models.CharField(max_length=255, blank=True)
    difficulty = models.CharField(max_length=32, choices=[
        ("Easy", "Easy"),
        ("Intermediate", "Intermediate"),
        ("Hard", "Hard")
    ], )
    favourite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="recipes")

    def __str__(self):
        return f"Recipe {self.id} : {self.title}"
