from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.foods.models import Ingredient


class Profile(models.Model):
    """Extends base User model with additional data."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")

    title = models.CharField(
        max_length=5, null=True, blank=True)
    dob = models.DateField(
        null=True, blank=True)
    address = models.CharField(
        max_length=255, null=True, blank=True)
    country = models.CharField(
        max_length=50, null=True, blank=True)
    city = models.CharField(
        max_length=50, null=True, blank=True)
    zipcode = models.CharField(
        max_length=5, null=True, blank=True)


class Inventory(models.Model):
    """User inventory."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    name = models.CharField(
        max_length=255, default="My inventory")

    ingredients = models.ManyToManyField(
        Ingredient, related_name="inventories")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Inventory.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.inventory.save()
