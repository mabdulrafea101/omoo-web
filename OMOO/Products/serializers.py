from rest_framework import serializers

from .models import Product, ProductCategory
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"



class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"