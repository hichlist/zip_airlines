from .models import Airplane
from .serializers import AirplaneSerializer

from rest_framework import viewsets


class AirplaneViewSet(viewsets.ModelViewSet):
    """
        Airplane API

        Arguments
        ---------

        * `Airplane id` - ID of an airplane (Field must be unique)
        * `Passengers` - Amount of passengers on board *(integer)*

        Errors
        ------

            {
                "airplane_id": [
                    "airplane with this airplane id already exists."
                ]
            }

    """

    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
