from django.contrib import admin
from blog.models import Post, PostAdmin

admin.site.register(Post, PostAdmin)
