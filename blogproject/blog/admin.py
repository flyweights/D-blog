from django.contrib import admin
from blog.models import Category, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
