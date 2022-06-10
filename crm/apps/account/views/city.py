from rest_framework import viewsets

from ..models import City
from ..serializers.city import CitySerializer


class CityModelViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    ordering = ['id']
    filterset_fields = ['name', 'id', 'country_id']
    search_fields = ['name', 'country__name']
