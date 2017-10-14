
# Librerias Django:
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static

from django.contrib import admin

from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls', namespace="home")),
    url(r'', include('redaccion.urls', namespace="redaccion")),
    url(r'', include('seguridad.urls', namespace="seguridad")),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
