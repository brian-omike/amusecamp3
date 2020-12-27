from django.contrib import admin
from .models import blog_post, Category, Profile, Comment

admin.site.register(blog_post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)