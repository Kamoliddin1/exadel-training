from rest_framework import serializers

from ..models import Country, City


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    country = serializers.IntegerField(source='country.id')
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        country = validated_data.pop('country')['id']
        city = validated_data.pop('name')
        instance = Country.objects.get(id=country)
        return City.objects.create(country=instance, name=city)

    def update(self, instance, validated_data):
        country = Country.objects.get(id=validated_data['country']['id'])
        instance.country = validated_data.get(country, instance.country)
        instance.name = validated_data.get(
            "name", instance.name
        )
        instance.save()
        return instance

