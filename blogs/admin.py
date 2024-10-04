from django.contrib import admin
from .models import Author, Blog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name',)
    list_filter = ('last_name',)
    search_fields = ('last_name', 'first_name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_name', 'is_published', 'author',)
    list_filter = ('blog_name',)
    search_fields = ('blog_name', 'author',)

