from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    data_create = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/',null=True, blank=True )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')   

    def __str__(self):
        return self.image
