from django.shortcuts import render
from .models import CryptoCurrency
from rest_framework import viewsets
from .serializers import CryptoCurrencySerializer
# Create your views here.
#from django.http import HttpResponse

class CryptoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
