from django.contrib import admin

from backend.apps.kitchen.models import(
    Category, Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'order_number']
    list_editable = ['order_number']
    prepopulated_fields = {'slug': ('name',)}




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'category', 'price', 'is_available']