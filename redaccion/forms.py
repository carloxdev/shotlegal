# -*- coding: utf-8 -*-

# Librerias Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Textarea
from django.forms import Select

# Modelos:
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = [
            'created_by',
            'updated_by',
        ]
        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control'}),
            'contenido': Textarea(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
        }
