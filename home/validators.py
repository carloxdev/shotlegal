# -*- coding: utf-8 -*-

# Librerias Django:
from django.core.exceptions import ValidationError


def validate_extension(obj):
    if (not obj.name.endswith('.png') and
        not obj.name.endswith('.jpeg') and
        not obj.name.endswith('.jpg') and
        not obj.name.endswith('.PNG') and
        not obj.name.endswith('.JPEG') and
            not obj.name.endswith('.JPG')):

        raise ValidationError("Solo se permiten archivos con extensión: .jpg, .jpeg, .png")


def validate_size(obj):
    filesize = obj.file.size
    megabyte_limit = 10.0
    bits_limit = megabyte_limit * 1024 * 1024
    if filesize > bits_limit:
        raise ValidationError("Tamaño máximo permitido %sMB" %
                              str(megabyte_limit))
