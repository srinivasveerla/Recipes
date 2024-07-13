from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer, RecipeListSerializer

class RecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
