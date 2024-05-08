from rest_framework.routers import DefaultRouter
from django.urls import path 
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.products.views import ProductAPI

router = DefaultRouter()
router.register('product', ProductAPI, basename='api_products')

# urlpatterns = [
#     path ('login/', TokenObtainPairView.as_view(), name ='api_login'),
#     path('refresh/', TokenRefreshView.as_view(), name = 'api_refresh')
# ]

urlpatterns = router.urls