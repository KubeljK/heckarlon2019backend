from django.db import IntegrityError

from rest_framework import serializers

from .models import Recipe, Ingredient, Nutrients, RecipeIngredient


class NutrientSerializer(serializers.ModelSerializer):
    """
    Nutrient.
    """
    class Meta:
        model = Nutrients
        fields = [
            'name', 'description', 'value', 'unit'
        ]

class IngredientSerializer(serializers.ModelSerializer):
    """
    Ingredient with it's nutrient values.
    """
    nutrients = NutrientSerializer(read_only=True, many=True)

    class Meta:
        model = Ingredient
        fields = [
            'url', 'name', 'description', 'manufacturer', 'nutrients'
        ]

class IngredientListSerializer(serializers.ModelSerializer):
    """
    Ingredient list, without nutrients.
    """
    class Meta:
        model = Ingredient
        fields = [
            'url', 'name', 'description', 'manufacturer'
        ]

class IngredientListNameOnlySerializer(serializers.ModelSerializer):
    """
    Ingredient list, only names and ids.
    """
    class Meta:
        model = Ingredient
        fields = [
            'id', 'name',
        ]

class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    RecipeIngredient with ingredient.
    """
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = [
            'ingredient', 'quantity', 'unit',
        ]

class RecipeSerializer(serializers.ModelSerializer):
    """
    Recipe with it's ingredients.
    """
    ingredients = RecipeIngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = [
            'url', 'name', 'instructions', 'preparation_time',
            'number_of_servings', 'source', 'image_url', 'ingredients'
        ]

class RecipeListSerializer(serializers.ModelSerializer):
    """
    Recipe list.
    """
    class Meta:
        model = Recipe
        fields = [
            'url', 'name', 'instructions', 'preparation_time',
            'number_of_servings', 'source', 'image_url'
        ]

# class RecipeIngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeIngredient
#         fields = [
#             'recipe', 'ingredient', 'ingredient_name', 'quantity', 'unit'
#         ]

#     def validate(self, data):
#         data_copy = data.copy()
#         for key, value in data_copy.items():
#             if value is None:
#                 data.pop(key)

#         if RecipeIngredient.objects.filter(**data).exists():
#             raise serializers.ValidationError("Duplicated object: %s"%dict(data))
#         return data