from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
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


class CategoryProductResultView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class SearchProductView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


class DeleteProductById(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


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
    authentication_classes = [SessionAuthentication]
