from rest_framework.viewsets import ModelViewSet

from ..models import Country
from ..serializers.country import CountrySerializer


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
