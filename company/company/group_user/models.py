from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=45)
	age = models.DecimalField()
	def __str__(self):
		return self.name
		
class Group(models.Model):
	name = models.CharField(max_length=45)
	def __str__(self):
		return self.name