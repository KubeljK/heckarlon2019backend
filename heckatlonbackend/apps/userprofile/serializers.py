from django.contrib.auth.models import User

from rest_framework import serializers

from apps.userprofile.models import Profile, Inventory, InventoryIngredient
from apps.foods.serializers import IngredientSerializer
from apps.foods.models import Ingredient


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('title', 'dob', 'address', 'country', 'city', 'zipcode',)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'url', 'username', 'email', 'first_name', 'last_name', 'profile',
        )
        read_only_fields = (
            'url', 'username', 'email',
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        profile = instance.profile
        profile.title = profile_data.get('title', profile.title)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zipcode = profile_data.get('zipcode', profile.zipcode)
        
        instance.save()

        return instance

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save() # This already creates an Profile instance.

        return user

class InventoryIngredientSerializer(serializers.ModelSerializer):
    """
    InventoryIngredient with ingredient.
    """
    ingredient = IngredientSerializer()

    class Meta:
        model = InventoryIngredient
        fields = [
            'id', 'ingredient', 'quantity', 'unit',
        ]

class InventorySerializer(serializers.ModelSerializer):
    """
    Inventory with ingredients
    """
    ingredients = InventoryIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Inventory
        fields = [
            'url', 'name', 'desc', 'ingredients'
        ]

class InventoryCreateSerializer(serializers.ModelSerializer):
    """
    Inventory without ingredients.
    """

    class Meta:
        model = Inventory
        fields = [
            'name', 'desc'
        ]

    def create(self, validated_data):

        instance = Inventory(**validated_data)
        instance.user = user=self.context["user"]
        instance.save()

        return instance

class InventoryListSerializer(serializers.ModelSerializer):
    """
    Inventory without ingredients.
    """
    class Meta:
        model = Inventory
        fields = [
            'url', 'name', 'desc'
        ]

class InventoryIngredientInsertSerializer(serializers.ModelSerializer):
    """
    InventoryIngredient with FK ids processing.
    """
    ingredient_id = serializers.IntegerField()
    inventory_id = serializers.IntegerField()
   
    class Meta:
        model = InventoryIngredient
        fields = [
            'id', 'inventory_id', 'ingredient_id', 'quantity', 'unit',
        ]
    
    def create(self, validated_data):

        inventory = Inventory.objects.get(id=validated_data["inventory_id"])
        ingredient = Ingredient.objects.get(id=validated_data["ingredient_id"])

        instance = InventoryIngredient(
            inventory=inventory,
            ingredient=ingredient,
            quantity=validated_data.get("quantity", "by taste"),
            unit=validated_data.get("unit", "g"))

        instance.save()

        return instance

class InventoryIngredientUpdateSerializer(serializers.ModelSerializer):
    """
    InventoryIngredient with only quantity and unit fields.
    """
   
    class Meta:
        model = InventoryIngredient
        fields = [
            'id', 'inventory_id', 'ingredient_id', 'quantity', 'unit',
        ]
        read_only_fields = [
            'id', 'ingredient', 'inventory',
        ]
