from django.db import models


class RecipeCategory(models.Model):
    name = models.CharField(
        max_length=255, unique=True)

    description = models.CharField(
        max_length=255, null=True)
    
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)

class Recipe(models.Model):
    name = models.CharField(
        max_length=255, unique=True)

    description = models.TextField(
        null=True)

    instructions = models.TextField(
        null=True)

    preparation_time = models.IntegerField(
        null=True)

    number_of_servings = models.IntegerField(
        null=True)
    
    source = models.CharField(
        null=True, max_length=255)

    image_url = models.CharField(
        null=True, max_length=255)

    categories = models.ManyToManyField(
        RecipeCategory, related_name="recipes")
    
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return("Recipe: {}".format(self.name))

class IngredientCategory(models.Model):
    name = models.CharField(
        max_length=255, unique=True)

    description = models.CharField(
        max_length=255, null=True)
    
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)
 
class Ingredient(models.Model):
    name = models.CharField(
        max_length=255, unique=True)

    description = models.CharField(
        max_length=255, null=True)

    manufacturer = models.CharField(
        max_length=255, null=True)

    categories = models.ManyToManyField(
        IngredientCategory, related_name="ingredients")

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return("Ingredient: {} ({})".format(self.name, self.manufacturer))

class Nutrients(models.Model):
    class Meta:
        unique_together = [['name', 'ingredient']]

    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="nutrients")

    name = models.CharField(
        max_length=255)

    description = models.CharField(
        max_length=255, null=True)

    value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)

    unit = models.CharField(
        max_length=255, null=True)

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)

class RecipeIngredient(models.Model):
    class Meta:
        unique_together = [['recipe', 'ingredient', 'quantity', 'unit']]

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients")

    ingredient_name = models.TextField(
        null=True) #TODO: This is only for testing, delete it before production!!!

    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipes")

    quantity = models.CharField(
        max_length=255, null=True, default="by taste")

    unit = models.CharField(
        max_length=255, null=True, default="g")

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    deleted_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return("Recipe: {}, Ingredient: {} {} {}".format(self.recipe, self.ingredient, self.quantity, self.unit))
