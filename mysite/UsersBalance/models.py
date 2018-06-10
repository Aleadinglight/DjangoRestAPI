from django.db import models

# Create your models here.

class Balance(models.Model):
	User_name = models.CharField(max_length=20)
	Amount = models.FloatField()

	
#class Account(models.Model):
#	im = models.ForeignKey(Balance, on_delete=models.CASCADE, related_name="ad")
#	Name = models.CharField(max_length=10)