from django.shortcuts import render
from PriceWatch.models import CryptoCurrency
from UsersBalance.models import Balance#, Account
from rest_framework import viewsets
from .serializers import CryptoCurrencySerializer, BalanceSerializer#, AccountSerializer
# Create your views here.
#from django.http import HttpResponse

class CryptoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer

class BalanceViewSet(viewsets.ModelViewSet):
	queryset = Balance.objects.all()
	serializer_class = BalanceSerializer
	
#class AccountViewset(viewsets.ModelViewSet):
#	queryset = Account.objects.all()
#	serializer_class = AccountSerializer