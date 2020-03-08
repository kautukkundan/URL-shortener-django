from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Url

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.PrimaryKeyRelatedField(many=True, queryset=Url.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'urls']

class UrlListSerializer(serializers.HyperlinkedModelSerializer):
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