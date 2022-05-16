from rest_framework import serializers
from ..models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username', 'is_user', 'is_company']
