# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import Disclaimer

urlpatterns = [
    url(r'^disclaimer/$', Disclaimer.as_view(), name="disclaimer"),
]
