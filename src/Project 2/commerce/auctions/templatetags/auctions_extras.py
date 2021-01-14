from django import template

register = template.Library()

@register.simple_tag
def number_of_watchlist_items(request):
    return 'cat'

"""
@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None
"""