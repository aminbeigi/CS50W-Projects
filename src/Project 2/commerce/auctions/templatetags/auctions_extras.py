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
        return {
            'item_in_wishlist': False
        }
    print(user, listing)
    
    item_watchlist = Watchlist.objects.filter(author__username__contains=user)
    print(item_watchlist)

    return {
        'item_in_watchlist': 'hi'
    }