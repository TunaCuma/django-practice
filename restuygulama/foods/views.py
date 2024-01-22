from django.shortcuts import render
from rest_framework import viewsets
from .models import Food, Category
from .serializers import FoodSerializer, CategorySerializer

# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer