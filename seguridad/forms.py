# -*- coding: utf-8 -*-

# Librerias Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Textarea
# from django.forms import FileInput
# from django.forms import Select

# Modelos:
from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = [
            'user',
            'comentarios',
            'is_owner',
        ]
        widgets = {
            'bio': Textarea(attrs={'class': 'form-control'}),
            'twitter_url': TextInput(attrs={'class': 'form-control'}),
            'facebook_url': TextInput(attrs={'class': 'form-control'}),
            'pinteres_url': TextInput(attrs={'class': 'form-control'}),
            'telefono': TextInput(attrs={'class': 'form-control'}),
        }
