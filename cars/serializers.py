from rest_framework import serializers
from .models import Car

class CarSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','make','model','year','price']