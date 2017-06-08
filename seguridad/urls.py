# -*- coding: utf-8 -*-

# Librerias Django
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

# Librerias Propias
from .views import Login
from .views import OwnerInfo

urlpatterns = [
    url(
        r'^login/$',
        Login.as_view(),
        name="login"
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': settings.PUBLICACIONES_URL},
        name='logout'
    ),
    url(
        r'^owner_info/$',
        OwnerInfo.as_view(),
        name="owner_info"
    ),
]
