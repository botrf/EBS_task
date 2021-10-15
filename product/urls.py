from django.urls import path, include
from rest_framework import routers 
from store import urls

from .views import ProductView, ProductDetailView, ProductCrudViewSet 
router = routers.DefaultRouter()
router.register('product', ProductCrudViewSet, basename='product')

urlpatterns = [
    path('', ProductView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]

