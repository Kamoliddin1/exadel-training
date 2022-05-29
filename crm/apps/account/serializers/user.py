from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)
    city_name = serializers.CharField(source='city.name', required=False)

    class Meta:
        model = User
        fields = ['user', 'username', 'city', 'city_name', 'street', 'house_number',
                  'total_area']