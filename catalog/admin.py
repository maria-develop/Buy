from django.contrib import admin
from .models import Category, Product, Parent


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'category',)
    list_filter = ('product_name',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_name', 'category', 'year_born')
    list_filter = ('product_name',)
    search_fields = ('product_name', 'category',)
