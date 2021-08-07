from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title', 'created_at')
    search_fields = ('title', 'created_at')
    delete_confirmation_template = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at', 'price', 'image')
    list_display_links = ('id', 'name', 'created_at', 'price')
    search_fields = ('name', 'price', 'created_at', 'price')
    delete_confirmation_template = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'created_at')
    delete_confirmation_template = ('name',)


class ChefAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'created_at')
    delete_confirmation_template = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ContactU, ContactAdmin)
admin.site.register(Chef)