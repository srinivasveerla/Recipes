# recipes/urls.py
from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/create/', RecipeCreate.as_view(), name='recipe-create'),
]
