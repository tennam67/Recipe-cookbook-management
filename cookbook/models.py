from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from recipe.models import Recipe


class CookBook(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=255, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    recipe = models.ManyToManyField(to=Recipe, related_name="cookbooks", blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="cookbooks")

