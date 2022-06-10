from rest_framework.viewsets import ModelViewSet
from ..models import Rating
from ..serializers.rating import RatingSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    search_fields = ['rate']
    ordering = ['id']
