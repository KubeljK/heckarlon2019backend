from django.urls import path

from apps.foods import views


urlpatterns = [

    # Check if connection works.
    path("health", views.Health.as_view(), name="health"),

    # Ingredients
    path("v1/ingredients/", views.IngredientList.as_view(), name="ingredient-list"),
    path("v1/ingredients/<int:pk>", views.IngredientDetails.as_view(), name="ingredient-detail"),

    # Recipes
    path("v1/recipes/", views.RecipeList.as_view(), name="recipe-list"),
    path("v1/recipes/<int:pk>", views.RecipeDetails.as_view(), name="recipe-detail"),

    # # GET and POST Recipes
    # path("data/recipe", views.recipes, name="data_recipe"),
    # # GET and POST Ingredients
    # path("data/ingredient", views.ingredients, name="data_ingredient"),
    # # POST Nutrients
    # path("data/nutrient", views.nutrients, name="data_nutrient"),
    # # GET and POST RecipeIngredient
    # path("data/recipeingredient", views.recipeingredients, name="data_recipeingredient"),

]
