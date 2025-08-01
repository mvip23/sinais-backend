from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiplica o valor pelo argumento fornecido.
    Uso: {{ value|multiply:arg }}
    """
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0 