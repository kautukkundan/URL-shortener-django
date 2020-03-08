from rest_framework import serializers

from core.models import Url

class UrlListSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model  = Url
    fields = (
      'id',
      'long_url',
      'short_url',
      'clicks'
    )