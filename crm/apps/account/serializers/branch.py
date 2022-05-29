from rest_framework import serializers
from ..models import Branch, Company


class BranchSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Branch
        fields = ['id', 'name', 'company']
