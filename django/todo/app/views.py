from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, authentication, permissions, generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import app
from .models import Item
from .serializer import UserSerializer
from models import User, UserManager


# Create your views here.

queryset = User.objects.all()
serializer_class = UserSerializer


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def items(request):
    return None
