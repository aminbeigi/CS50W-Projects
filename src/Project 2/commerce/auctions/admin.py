from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Listing, Comment, Bid

admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)