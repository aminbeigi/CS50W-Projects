from .models import Watchlist

def calculate_watchlist_count(request):
    user = str(request.user)

    if user == 'AnonymousUser':
        return {
            'watchlist_count': '0'
        }

    watchlist_count = len(Watchlist.objects.filter(author__username__contains=user))
    return {
        'watchlist_count': watchlist_count
    }