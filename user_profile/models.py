from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

import random

from django.db import models

# This will guarantee that it will check the settings and assign the user we have created
from django.db.models.signals import post_save
from django.dispatch import receiver

from cookbook.models import CookBook
from recipe.models import Recipe

User = get_user_model()


# Create your models here.


def code_generator(length=5):
    numbers = "123456789"
    return "".join(random.choice(numbers) for _ in range(length))


class UserProfile(models.Model):
    code = models.CharField(max_length=6, default=code_generator)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    favourite_cookbook = models.ManyToManyField(to=CookBook, related_name="liked_by", blank=True)
    favourite_recipe = models.ManyToManyField(to=Recipe, related_name="liked_by", blank=True)

    # CASCADE if the user gets deleted then it should automatically delete the user profile

    def __str__(self):
        return f"{self.id}: profile from {self.user.username}"

    # Django signal - singal dispatcher : it will notifies different apps when new user is created
    # A decorator for connecting receivers to signals. Used by passing in the
    #     signal (or list of signals) and keyword arguments to connect:
    #         @receiver(post_save, sender=MyModel)
    #         def signal_receiver(sender, **kwargs):
    # sender: use model is created or update it will send signal to django apps

    @receiver(post_save, sender=User)
    def create_registration_profile(sender, instance, **kwargs):
        profile, created = UserProfile.objects.get_or_create(user=instance)
        # created is boolean to check if it's created or not
        if created:
            profile.save()
            # if it's new profile then save it

