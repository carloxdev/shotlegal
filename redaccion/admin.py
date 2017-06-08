# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin

# Modelos:
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'contenido',
        'created_by',
        'created_date',
        'updated_date',
        'updated_by',
    )
