from rest_framework import serializers
from .models import Recipe, Step, Quantity, Author, Ingredient, Measurement

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email']

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['step_number', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['unit']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']

class QuantitySerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    measurement = MeasurementSerializer()

    class Meta:
        model = Quantity
        fields = ['ingredient', 'measurement', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    steps = StepSerializer(many=True)
    quantities = QuantitySerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'date', 'description', 'author', 'steps', 'quantities']
