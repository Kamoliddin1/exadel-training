from rest_framework import serializers
from ..models import Branch, Company


class BranchSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    company_name = serializers.CharField(source='company.title', required=False)

    class Meta:
        model = Branch
        fields = ['id', 'name', 'company', 'company_name']
