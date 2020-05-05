from django.contrib import admin
from .models import ProductGroup, Product


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ['label', 'slug']
    prepopulated_fields = {'slug': ('label',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['label', 'slug', 'cost', 'accessible', 'created', 'updated']
    list_filter = ['accessible', 'created', 'updated']
    list_editable = ['cost', 'accessible']
    prepopulated_fields = {'slug': ('label',)}
