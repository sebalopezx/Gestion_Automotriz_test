from django import template

register = template.Library()

@register.filter
def state_display(value):
    return "Completo" if value else "Incompleto"
