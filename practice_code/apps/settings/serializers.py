from rest_framework import serializers
from .models import Shop, Products

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'address']
        read_only_fields = ['id']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price']
        read_only_fields = ['id']
