from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Shop, Products
from .serializers import ShopSerializer, ProductsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProductsViewSet(
        CreateModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        viewsets.GenericViewSet  # <- Добавлено!
    ):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]