from django.urls import path
from .views import ShowAllProducts, CreateNewProduct, UpdateProductById, DeleteProductById, CategoryProductResultView, SearchProductView, UpdateUserInfo, SeeUserInfo

urlpatterns = [
    path('api/products', ShowAllProducts.as_view()),
    path('api/new', CreateNewProduct.as_view()),
    path('api/<int:pk>/update', UpdateProductById.as_view()),
    path('api/category/<str:name>', CategoryProductResultView.as_view()),
    path('api/search/<str:title>', SearchProductView.as_view()),
    path('api/delete/<int:id>/cart', DeleteProductById.as_view()),
    path('api/user/<username>', SeeUserInfo.as_view()),
    path('api/user/<username>/update', UpdateUserInfo.as_view()),
]
