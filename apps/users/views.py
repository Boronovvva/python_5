from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.users.models import User
from apps.users.serializers import UserSerializer,UserRegisterSerializer


class UserAPI(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer