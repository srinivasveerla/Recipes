from django.contrib import admin

# Register your models here.
from .models import Author, Recipe, Step, Ingredient

admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
