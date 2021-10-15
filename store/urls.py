
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from product.urls import router as product_router

schema_view = get_schema_view(
   openapi.Info(
      title="Product Task API",
      default_version='v1',
      description="""
       Create a project application store that will:
      - the products have name, price, description, date when it was added, pictures

      Create an API in which you can:
      - make CRUD a list of products (consisting of: name, sku, price, description)
      - will display the list of products with pagination (name, price, first picture)
      - will display the details of a product (name, price, description, date, all pictures)
      """,
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('product/crud/', include(product_router.urls)),
   path('product/', include('product.urls') , name='product-api'), 
   path('api-auth/', include('rest_framework.urls')),
   path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)