from rest_framework import serializers
from .models import Personnels

class PersonnelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnels
        fields = '__all__'