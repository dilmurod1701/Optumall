from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response

from .models import Users, Profile, Products, Cart
from .serializers import UserSerializer, ProfileSerializer, ProductsSerializer, CartSerializer


# Create your views here.


class ShowAllProducts(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CreateNewProduct(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminUser]


class UpdateProductById(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class DeleteProductById(DestroyAPIView):
    queryset = Products
    serializer_class = ProductsSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


class Category(APIView):
    def get(self, request, category):
        products = Products.objects.filter(category=category)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)


class SearchByTitle(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class SeeUserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = Users.objects.get(first_name=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UpdateUserInfo(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
