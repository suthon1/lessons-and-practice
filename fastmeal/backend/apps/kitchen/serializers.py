from rest_framework import serializers

from backend.apps.kitchen.models import Category, Product

class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'order_number', 'icon']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    category = CategorySeializer()
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'image',
            'price',
            'category',
        ]
        read_only_fields =['id']
