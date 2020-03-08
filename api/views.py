from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import permissions

from api.serializers import UrlListSerializer, UserSerializer

from api.permissions import IsOwner

import random
import string

from core.models import Url

class UserCreateAPIView(generics.CreateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

class UrlShortenerApiViewSet(ModelViewSet):
    serializer_class       = UrlListSerializer

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes     = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return Url.objects.all().filter(owner=user)

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)