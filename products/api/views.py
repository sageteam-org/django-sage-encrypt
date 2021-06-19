"""
Auto Generated views.py
You may need to change some parts
"""

from rest_framework.viewsets import ModelViewSet

from products.models import *
from products.api.serializers import *


class CategoryViewset(ModelViewSet):
    """
    Category Viewset
    Auto generated
    """
    serializer_class = CategorySerializer

    queryset = Category.objects.all()


class ProductViewset(ModelViewSet):
    """
    Product Viewset
    Auto generated
    """
    serializer_class = ProductSerializer

    queryset = Product.objects.all()


class DiscountViewset(ModelViewSet):
    """
    Discount Viewset
    Auto generated
    """
    serializer_class = DiscountSerializer

    queryset = Discount.objects.all()
