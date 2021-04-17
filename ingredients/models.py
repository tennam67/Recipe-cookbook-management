from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=255, blank=False)
    favourite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"Recipe {self.id} : {self.name}"
