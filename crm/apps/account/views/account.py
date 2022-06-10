from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from ..models import Account
from ..serializers.account import AccountSerializer


class AccountViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()

    def list(self, request):
        serializer = AccountSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        acc = get_object_or_404(self.queryset, pk=pk)
        serializer = AccountSerializer(acc)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = AccountSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
