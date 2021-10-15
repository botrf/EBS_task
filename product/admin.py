from django.contrib import admin

from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'data_create', 'sku')


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
