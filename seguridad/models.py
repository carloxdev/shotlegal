# -*- coding: utf-8 -*-

# Libreria Django:
from __future__ import unicode_literals
from django.db import models

# Libreria Django Signals:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Otros modelos:
from django.contrib.auth.models import User

# Validadores:
from home.validators import validate_extension
from home.validators import validate_size


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    comentarios = models.TextField(blank=True)
    is_owner = models.BooleanField(default=False)
    imagen = models.ImageField(
        upload_to='perfil/img',
        blank=True,
        validators=[
            validate_extension,
            validate_size
        ]
    )
    twitter_url = models.CharField(max_length=144, blank=True, null=True)
    facebook_url = models.CharField(max_length=144, blank=True, null=True)
    pinteres_url = models.CharField(max_length=144, blank=True, null=True)
    telefono = models.CharField(max_length=144, blank=True, null=True)

    def __str_(self):
        nombre_completo = self.user.get_full_name()
        return nombre_completo

    def __unicode__(self):
        nombre_completo = self.user.get_full_name()
        return nombre_completo


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
