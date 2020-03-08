from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Url

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class UrlListSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model  = Url
    fields = (
      'id',
      'long_url',
      'short_url',
      'clicks',
      'owner'
    )