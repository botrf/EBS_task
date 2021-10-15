from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product',)


class ProductCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'price', 'description')


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product 
        fields = ('id', 'name', 'sku', 'price', 'image')

    def get_image(self, obj):
        image = ProductImage.objects.filter(product=obj).first()
        if image:
            serializer = ProductImageSerializer(image)
            return serializer.data

        return None


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'data_create', 'images')

