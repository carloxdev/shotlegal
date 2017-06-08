# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.shortcuts import render
from django.shortcuts import redirect

from django.core.urlresolvers import reverse

from django.views.generic.base import View

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Own's Libraries
from .models import Profile
from .forms import ProfileForm


class Login(View):

    template_name = 'login.html'

    def get(self, request):

        if request.user.is_authenticated():
            return redirect(reverse('redaccion:post_administracion'))

        else:
            return render(request, self.template_name, {})

    def post(self, request):

        cuenta = request.POST.get('cuenta')
        contrasena = request.POST.get('contrasena')

        user = authenticate(username=cuenta, password=contrasena)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect(reverse('redaccion:post_administracion'))
            else:
                messages.warning(
                    request,
                    'Cuenta DESACTIVADA, favor de contactar a su administrador'
                )
        else:
            messages.error(
                request,
                "Cuenta usuario o contraseña no valida"
            )

        return render(request, self.template_name, {})


class OwnerInfo(View):

    template_name = 'owner_info.html'

    def get_UrlImagen(self, _imagen):
        imagen = ""
        if _imagen:
            imagen = _imagen.url

        return imagen

    def get(self, _request):

        profile = Profile.objects.get(is_owner=True)

        formulario = ProfileForm(instance=profile)

        contexto = {
            'form': formulario,
            'imagen': self.get_UrlImagen(profile.imagen)
        }

        return render(_request, self.template_name, contexto)

    def post(self, _request):

        profile = Profile.objects.get(is_owner=True)

        formulario = ProfileForm(_request.POST, _request.FILES)

        if formulario.is_valid():
            upd_profile = formulario.save(commit=False)

            profile.bio = upd_profile.bio
            profile.imagen = upd_profile.imagen
            profile.twitter_url = upd_profile.twitter_url
            profile.facebook_url = upd_profile.facebook_url
            profile.pinteres_url = upd_profile.pinteres_url
            profile.telefono = upd_profile.telefono
            profile.save()

            return redirect(reverse('redaccion:post_publicados'))

        contexto = {
            'form': formulario,
            'imagen': self.get_UrlImagen(profile.imagen)
        }

        return render(_request, self.template_name, contexto)
