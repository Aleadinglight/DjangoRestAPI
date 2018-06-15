from .model import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerialier):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')
		
class GroupSerializer(serializers.HyperlinkedModelSerialier):
	class Meta:
		model = Group
		fields = ('url', 'name')