from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from fruit_restapi.models import Fruit
from fruit_restapi.serializers import FruitSerializer
from rest_framework.permissions import AllowAny

class FruitListAll(generics.ListAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = [AllowAny]

class FruitRetrive(generics.RetrieveAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = [AllowAny]

class FruitCreate(generics.CreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = [AllowAny]

