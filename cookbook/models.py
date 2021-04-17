from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

from django.db import models

from recipe.models import Recipe
from user.models import user_directory_path

User = get_user_model()


# Create your models here.


class CookBook(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=255, blank=False)
    book_cover = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    recipe = models.ManyToManyField(to=Recipe, related_name="cookbooks", blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="cookbooks")
