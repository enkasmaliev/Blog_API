from django.contrib import admin
from .models import Article, Tag, Comment

admin.site.register([Article, Tag, Comment])
