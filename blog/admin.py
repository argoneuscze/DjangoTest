from django.contrib import admin

from .models import Squad, User, Article, Comment

admin.site.register((Squad, User, Article, Comment))
