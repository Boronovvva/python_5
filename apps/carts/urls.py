from django.urls import path
from apps.carts.views import CartViewSet, CartDetailAPI,CartItemViewSet,CartItemDetailAPI


urlpatterns = [
    path('api/carts/', CartViewSet.as_view(), name='api/carts/'),
    path('api/carts/<int:pk>/', CartDetailAPI.as_view(), name="api_carts_detail"),
    path('api/cartitem/', CartItemViewSet.as_view(), name='api/cartitem/'),
    path('api/cartitem/<int:pk>/', CartItemDetailAPI.as_view(), name="api_cartitem_detail"),

]



