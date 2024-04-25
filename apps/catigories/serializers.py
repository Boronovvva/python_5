from rest_framework import serializers

from apps.catigories.models import Catigory

class CatigorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catigory
        fields = ('id','title', 'slug','parent')