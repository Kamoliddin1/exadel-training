from rest_framework import viewsets

from ..models import City
from ..serializers.city import CitySerializer


class CityModelViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
