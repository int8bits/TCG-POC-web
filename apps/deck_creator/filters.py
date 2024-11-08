
import ast

from django import template

register = template.Library()


@register.filter
def split_list(value):
    try:
        return ast.literal_eval(value)
    except Exception:
        return []
