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
        fields = ['id', 'name', 'date', 'description', 'author', 'steps', 'quantities', 'display_picture']

class RecipeListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'date', 'description', 'author', 'display_picture']


class RecipeCreateSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True)
    author_email = serializers.EmailField(write_only=True)
    steps = serializers.ListField(child=serializers.CharField(), write_only=True)
    ingredients = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'date', 'display_picture', 'description', 'author_name', 'author_email', 'steps', 'ingredients']

    def create(self, validated_data):
        author_name = validated_data.pop('author_name')
        author_email = validated_data.pop('author_email')
        steps_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')

        author, created = Author.objects.get_or_create(name=author_name, email=author_email)

        recipe = Recipe.objects.create(author=author, **validated_data)

        for step_number, description in enumerate(steps_data, start=1):
            Step.objects.create(recipe=recipe, step_number=step_number, description=description)

        for ingredient_data in ingredients_data:
            ingredient_name = ingredient_data.get('name')
            quantity = ingredient_data.get('quantity')
            measurement_unit = ingredient_data.get('measurement')

            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
            measurement, created = Measurement.objects.get_or_create(unit=measurement_unit)

            Quantity.objects.create(recipe=recipe, ingredient=ingredient, measurement=measurement, quantity=quantity)

        return recipe
