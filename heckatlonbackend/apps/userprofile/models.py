from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.foods.models import Ingredient


class Profile(models.Model):
    """
    Extends base User model with additional data.
    """

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
    """
    User inventory.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="inventories")

    name = models.CharField(
        max_length=255, default="My inventory")
    
    desc = models.CharField(
        max_length=255, default="This inventory is automatically created", null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)

class InventoryIngredient(models.Model):
    """
    Connects Inventory and Ingredient models
    """

    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name="ingredients")

    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="inventories")

    quantity = models.CharField(
        max_length=255, null=True, default="by taste")

    unit = models.CharField(
        max_length=255, null=True, default="g")

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Inventory.objects.create(user=instance, name="My first inventory")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
