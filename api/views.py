from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from api.serializers import UrlListSerializer
from rest_framework.response import Response

import random
import string

from core.models import Url

# Create your views here.
class UrlShortenerApiViewSet(ModelViewSet):
  queryset         = Url.objects.all()
  serializer_class = UrlListSerializer

  # def post(self, request, *args, **kwargs):
  #   form_data = request.POST

  #   long_url  = form_data['long_url']
  #   short_url = form_data['short_url'].replace(" ", "_")

  #   if(not short_url):
  #     short_url = ''.join(random.choices(string.ascii_lowercase+string.digits, k=8))

  #   exists = Url.objects.filter(short_url=short_url)

  #   if(not exists):
  #     serializer = UrlListSerializer(long_url=long_url, short_url=short_url)
  #     if serializer.is_valid():
  #         serializer.save()
  #         return Response(serializer.data)
  #   else:
  #     return Response(serializer.error)
  