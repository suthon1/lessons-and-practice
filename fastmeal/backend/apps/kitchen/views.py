from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

from backend.apps.kitchen.serializers import CategorySeializer, ProductSerializer
from backend.apps.kitchen.models import (Category, Product)

def index(request):
    return HttpResponse('Hello')

class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeializer


class CategoryCreateApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeializer


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('category_slug')
        if slug:
            product = Product.objects.filter(is_available=True, category_slug=slug)
        return product