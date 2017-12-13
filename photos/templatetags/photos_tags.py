from django import template


register = template.Library()


@register.filter
def percentage(value):
    """Change fraction to percentage."""
    return '{}%'.format(round(value * 100))
