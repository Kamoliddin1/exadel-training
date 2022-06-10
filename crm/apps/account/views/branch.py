from rest_framework.viewsets import ModelViewSet

from ..models import Branch
from ..serializers.branch import BranchSerializer


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    search_fields = ['name', 'company__title']
    ordering = ['id']
