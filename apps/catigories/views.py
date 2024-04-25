from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.catigories.models import Catigory
from apps.catigories.serializers import CatigorySerializer

class CatigoryViewSet(ListCreateAPIView):
    queryset = Catigory.objects.all()
    serializer_class = CatigorySerializer

class CatigoryDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Catigory.objects.all()
    serializer_class = CatigorySerializer