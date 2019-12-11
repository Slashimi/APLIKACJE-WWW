  
from rest_framework import serializers
from .models import Towary, Kupony


class TowarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Towary
        fields = '__all__'



class KuponySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kupony
        fields = '__all__'