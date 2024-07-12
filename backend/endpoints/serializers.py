# recipes/serializers.py
from rest_framework import serializers
from .models import Author, Recipe, Step, Ingredient

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['step_number', 'description']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'date','description', 'display_picture', 'author', 'steps', 'ingredients']
