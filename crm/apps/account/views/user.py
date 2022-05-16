from rest_framework import viewsets

from ..models import User
from ..serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
