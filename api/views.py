from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import UrlListSerializer, UserSerializer

from rest_framework import permissions
from api.permissions import IsOwner

import random
import string

from core.models import Url

# Create your views here.
class UserList(generics.ListAPIView):
  queryset         = User.objects.all()
  serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
  queryset         = User.objects.all()
  serializer_class = UserSerializer

class UrlShortenerApiViewSet(ModelViewSet):
  serializer_class       = UrlListSerializer

  authentication_classes = (TokenAuthentication,)
  permission_classes     = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)

  def get_queryset(self):
    user = self.request.user
    return Url.objects.filter(owner=user)

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
  