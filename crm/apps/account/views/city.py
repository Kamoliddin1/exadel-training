from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )

from ..models import City
from ..serializers.city import CitySerializer


class CityListCreateAPIView(ListCreateAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
