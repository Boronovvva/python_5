# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from apps.catigories.models import Catigory
# from apps.catigories.serializers import CatigorySerializer

# class CatigoryViewSet(ListCreateAPIView):
#     queryset = Catigory.objects.all()
#     serializer_class = CatigorySerializer

# class CatigoryDetailAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Catigory.objects.all()
#     serializer_class = CatigorySerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.catigories.models import Catigory
from apps.catigories.serializers import CatigorySerializer

class CatigoryAPI(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Catigory.objects.all()
    serializer_class = CatigorySerializer