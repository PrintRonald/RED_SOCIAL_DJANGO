# S ecrea este arcvhivo para poder crear un perfil cuando un 
# ususario se registra en la aplicacion

from django.contrib.auth import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)