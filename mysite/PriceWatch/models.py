from django.db import models

# Create your models here.
class CryptoCurrency(models.Model):
	Coin_name = models.CharField(max_length=5)
	Price = models.FloatField()
	Volume = models.IntegerField()
	Change = models.FloatField()
