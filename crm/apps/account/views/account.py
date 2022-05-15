from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Account
from ..serializers.account import AccountSerializer


class AccountListCreateAPIView(ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
