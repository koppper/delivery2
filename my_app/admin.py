from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'restaurant', 'description', 'price', 'created_at', 'updated_at',
                    'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'tag')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category_rest', 'slug', 'created_at', 'is_published',
                    'updated_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'type')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'Фото'


class CartItemAdmin(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin, ]


class ProductAdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductTag)
admin.site.register(ProductCategory, ProductAdminCategory)

admin.site.register(Restaurants, RestaurantsAdmin)
admin.site.register(RestaurantType)
admin.site.register(RestaurantCategory)

admin.site.register(Cart, CartAdmin)
