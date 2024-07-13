from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    display_picture = models.URLField(max_length=255, blank=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    step_number = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('recipe', 'step_number')
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number} for {self.recipe.name}"


class Measurement(models.Model):
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.unit


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='quantities')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='quantities')
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='quantities')
    quantity = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('recipe', 'ingredient', 'measurement')

    def __str__(self):
        return f"{self.quantity} {self.measurement} of {self.ingredient} for {self.recipe.name}"
