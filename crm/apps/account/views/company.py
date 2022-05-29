from rest_framework import viewsets

from ..models import Company
from ..serializers.company import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
