# serializers.py
from rest_framework import serializers

from .models import Loads

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loads
        fields = '__all__'