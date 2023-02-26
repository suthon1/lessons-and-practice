from django.urls import path

# from backend.apps.kitchen.views import index, CategoryListApiView, CategoryCreateApiView, ProductListApiView
from backend.apps.kitchen import views


urlpatterns = [
    # path('', index, name='index'),
    path('api/v1/category-list', views.CategoryListApiView.as_view(), name='category-list'),
    path('api/v1/create-category-list/', views.CategoryCreateApiView.as_view(), name='create-category'),
    path('api/v1/product-list/',views.ProductListApiView.as_view(), name='product-list'),
    path('api/v1/list/<slug:category_slug>/', views.ProductListApiView.as_view()),
]