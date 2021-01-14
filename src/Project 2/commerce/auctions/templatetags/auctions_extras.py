from django import template
from . import Watchlist

register = template.Library()

"""
@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None
"""

@register.filter
def item_in_watchlist(user, listing):
    if user == 'AnonymousUser':
        return False
        
    watchlist = Watchlist.objects.filter(author__username__contains=user)
    for i in watchlist:
        if (i.listing == listing):
            return True
    return False