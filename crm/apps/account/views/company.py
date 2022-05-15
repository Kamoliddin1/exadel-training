from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.response import Response

from ..models import Company
from ..serializers.company import CompanySerializer


class CompanyListCreateAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)


class CompanyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
