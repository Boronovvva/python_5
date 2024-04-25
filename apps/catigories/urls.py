from django.urls import path
from apps.catigories.views import CatigoryViewSet, CatigoryDetailAPI


urlpatterns = [
    path('api/categories/', CatigoryViewSet.as_view(), name='api/categories/'),
    path('api/categories/<int:pk>/', CatigoryDetailAPI.as_view(), name="api_category_detail")
]
