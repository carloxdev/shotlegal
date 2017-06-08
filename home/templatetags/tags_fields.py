# Django's Libraries
from django import template


register = template.Library()


@register.inclusion_tag(
    'tags/tag_input.html',
    takes_context=False)
def tag_input(_field):

    contexto = {
        'campo': _field
    }
    return contexto


@register.inclusion_tag(
    'tags/tag_image.html',
    takes_context=False)
def tag_image(_field, _imagen):

    contexto = {
        'campo': _field,
        'imagen': _imagen
    }
    return contexto
