from django.contrib import admin
from .models import Category, Product, Brand
from .forums import CategoryAdminForm, ProductAdminForm, BrandAdminForm
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'old_price', 'created_date', 'updated_date',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-created_date']
    search_fields = ['name', 'description', 'meta_description', 'meta_keywords']
    exclude = ('created_date', 'updated_date',)

    prepopulated_fields = {'slug':('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

    list_display = ('name', 'created_date', 'updated_date',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_description', 'meta_keywords']
    exclude = ('created_date', 'updated_date',)

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    form = BrandAdminForm

    list_display = ('name', 'created_date', 'updated_date',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_description', 'meta_keywords']
    exclude = ('created_date', 'updated_date',)

    prepopulated_fields = {'slug': ('name',)}