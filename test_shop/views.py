from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import ProductSerializers, DetailProductSerializer
from .models import Product


class ListProductView(generics.ListCreateAPIView):
    """
        Get list of products, search by 'art' and 'name', filter by status
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['art', 'name']


class DetailProductView(generics.RetrieveUpdateAPIView):
    """
        Get detail of products
    """
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = (AllowAny,)
