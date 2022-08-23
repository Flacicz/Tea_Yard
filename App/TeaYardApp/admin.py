from django.contrib import admin

from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'available', 'price', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('available',)
    list_filter = ('available', 'category')
    fields = ('title', 'category', 'description', 'photo', 'available', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление товаром'
admin.site.site_header = 'Управление товаром'
