from .models import Airplane
from rest_framework import serializers


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'
        read_only_fields = ('fuel_tank', 'consumption', 'minutes_to_fly',)
