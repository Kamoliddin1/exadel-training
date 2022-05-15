from rest_framework import serializers
from ..models import Account


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    is_user = serializers.BooleanField(default=False)
    is_company = serializers.BooleanField(default=False)

    def create(self, validated_data):
        account = Account(**validated_data)
        account.save()
        return account

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.is_user = validated_data.get('is_user', instance.is_user)
        instance.is_company = validated_data.get('is_company', instance.is_company)

        instance.save()
        return instance
