from rest_framework.viewsets import ModelViewSet 
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.mixins import RetrieveModelMixin 

from .models import Product 
from .serializers import ProductSerializer, ProductDetailSerializer, ProductCRUDSerializer


class ProductCrudViewSet(ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductCRUDSerializer


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveModelMixin, GenericAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    def get(self, request, *args, **kwargs):
        return super().retrieve(request,request, *args, **kwargs)
        
    
