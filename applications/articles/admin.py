from django.contrib import admin
from .models import Article, Tag, Comment, Like, Rating

admin.site.register([Article, Tag, Comment, Like, Rating])
