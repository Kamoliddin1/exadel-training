from rest_framework import serializers
from ..models import Company, Account, City


class CompanySerializer(serializers.Serializer):
    company = serializers.IntegerField(source='company.id')
    title = serializers.CharField(max_length=200)
    street = serializers.CharField(max_length=200)
    city = serializers.IntegerField(source='city.id')

    def create(self, validated_data):
        # One user can have one company
        company_id = validated_data.pop('company')['id']
        title = validated_data.pop('title')
        city_id = validated_data.pop('city')['id']
        instance = Account.objects.get(id=company_id)
        city = City.objects.get(id=city_id)
        return Company.objects.create(company=instance, title=title, city=city, **validated_data)

    def update(self, instance, validated_data):
        company = Account.objects.get(id=validated_data.get('company')['id'])
        city = City.objects.get(id=validated_data.get('city')['id'])
        instance.company = company
        instance.city = city
        instance.title = validated_data.get('title', instance.title)
        instance.street = validated_data.get('street', instance.street)

        instance.save()
        return instance
