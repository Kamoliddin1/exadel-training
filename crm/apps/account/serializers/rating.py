from rest_framework import serializers
from ..models import User, Rating


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    rate = serializers.ChoiceField(choices=Rating.rate_choices)
    review = serializers.CharField(max_length=500)
    timestamp = serializers.DateTimeField()

    class Meta:
        model = Rating
        fields = ['id', 'author', 'review', 'rate', 'timestamp']
