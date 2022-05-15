from rest_framework import serializers
from ..models import User, Account, City


class UserSerializer(serializers.Serializer):
    user = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username', required=False)
    city = serializers.IntegerField(source='city.id')
    city_name = serializers.CharField(source='city.name', required=False)
    street = serializers.CharField(max_length=200)
    house_number = serializers.CharField(max_length=50)
    total_area = serializers.FloatField()

    def create(self, validated_data):
        user_id = validated_data.pop('user')['id']
        city_id = validated_data.pop('city')['id']
        instance = Account.objects.get(id=user_id)
        city = City.objects.get(id=city_id)
        return User.objects.create(user=instance, city=city, **validated_data)

    def update(self, instance, validated_data):
        user = Account.objects.get(id=validated_data.get('user')['id'])
        city = City.objects.get(id=validated_data.get('city')['id'])
        instance.user = user
        instance.city = city
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.total_area = validated_data.get('total_area', instance.total_area)

        instance.save()
        return instance
