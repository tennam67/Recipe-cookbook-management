import random

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from cookbook.models import CookBook
from recipe.models import Recipe


def code_generator(length=5):
    numbers = "123456789"
    return "".join(random.choice(numbers) for _ in range(length))


class UserProfile(models.Model):
    code = models.CharField(max_length=6, default=code_generator)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    favourite_cookbook = models.ManyToManyField(to=CookBook, related_name="liked_by", blank=True)
    favourite_recipe = models.ManyToManyField(to=Recipe, related_name="liked_by", blank=True)
    # CASCADE if the user gets deleted then it should automatically delete the user profile

