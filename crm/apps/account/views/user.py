from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.response import Response

from ..models import User
from ..serializers.user import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
