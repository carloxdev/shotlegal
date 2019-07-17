
# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Librerias Propias

# Otros Modelos:
from seguridad.models import Profile

# Validadores:
from home.validators import validate_extension
from home.validators import validate_size

from .utilities import get_ImagePath_Post


class Post(models.Model):

    STATUS = (
        ('PUB', 'PUBLICADO'),
        ('REC', 'Redactando'),
    )

    titulo = models.CharField(max_length=120)
    imagen = models.ImageField(
        upload_to=get_ImagePath_Post,
        blank=True,
        validators=[
            validate_extension,
            validate_size
        ]
    )
    contenido = models.TextField()

    status = models.CharField(max_length=3, choices=STATUS, default="REC")
    created_by = models.ForeignKey(
        Profile,
        related_name='post_creador',
        on_delete=models.PROTECT,
        null=True
    )
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(
        Profile,
        related_name='post_actualizador',
        on_delete=models.PROTECT,
        null=True
    )
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo
