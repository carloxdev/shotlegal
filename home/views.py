
# Librerias Django
from django.shortcuts import render
from django.views.generic.base import View


class Disclaimer(View):
    template_name = 'disclaimer.html'

    def get(self, request):
        return render(request, self.template_name, {})
