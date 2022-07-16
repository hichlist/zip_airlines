from .models import Airplane
from .serializers import AirplaneSerializer

from rest_framework import viewsets


class AirplaneViewSet(viewsets.ModelViewSet):

    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
