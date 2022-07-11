from django import template

from users.models import DeliveryAddress

register = template.Library()

@register.simple_tag()
def get_address():
    return DeliveryAddress.objects.all()
