from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    return f"{instance.id}/{filename}"


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.email}"
