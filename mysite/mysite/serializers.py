from PriceWatch.models import CryptoCurrency
from UsersBalance.models import Balance#, Account
from rest_framework import serializers

class CryptoCurrencySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CryptoCurrency
		fields = ('url','Coin_name','Price','Volume','Change')
		
class BalanceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Balance
		fields = ('url','User_name','Amount')
		
#class AccountSerializer(serializers.HyperlinkedModelSerializer):
#	class Meta:
#		model = Account
#		fields = ('url','im','Name')