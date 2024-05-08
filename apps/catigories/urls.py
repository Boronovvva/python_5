from rest_framework.routers import DefaultRouter
from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from apps.catigories.views import CatigoryAPI

router = DefaultRouter()
router.register('catigories', CatigoryAPI, basename='api_catigories')


urlpatterns = router.urls
