from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from rest_framework import status, viewsets, mixins, filters, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes, parser_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request

import requests, json
import logging
logger = logging.getLogger("data_logger")

from apps.userprofile.permissions import IsDeveloperOrAdmin
from .models import RecipeCategory, Recipe, IngredientCategory, Ingredient, Nutrients, RecipeIngredient
from .serializers import IngredientListSerializer, IngredientSerializer,\
    RecipeIngredientSerializer, RecipeSerializer, RecipeListSerializer, IngredientListNameOnlySerializer
from .services import DataPosterService, DataGetterService


class Health(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(
            {
                "message": "Hello!",
                "user": str(request.user),
                "auth": str(request.auth)
            },
            status.HTTP_200_OK
        )

    def post(self, request):
        return Response(
            {
                "message": "Hello! You posted.",
                "data": request.data,
                "user": str(request.user),
                "auth": str(request.auth)
            },
            status.HTTP_200_OK
        )

class IngredientList(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = IngredientListSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name', 'manufacturer']

class IngredientListNames(generics.ListAPIView):
    """
    Returns list of ALL ingredients (names and their respective ids).
    """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = IngredientListNameOnlySerializer
    queryset = Ingredient.objects.exclude(name__icontains=" ") #

    pagination_class = None

class IngredientDetails(generics.RetrieveAPIView):

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

class RecipeList(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RecipeListSerializer
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name']

    def post(self, request):
        ingredient_ids = request.data.get("ingredient_ids", [])
        queryset = Recipe.objects.all()

        for ingredient_id in ingredient_ids:
            queryset = queryset.filter(ingredients__ingredient__id=ingredient_id)

        # TODO: This is for development only!
        # Make a proper weight funtion.
        queryset = queryset[:20]

        ingredients = self.serializer_class(
            queryset, many=True, context={'request': request,}
            )
        return Response(ingredients.data, status.HTTP_200_OK)

class RecipeDetails(generics.RetrieveAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()



# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# # @permission_classes([IsDeveloperOrAdmin])
# def recipes(request):
#     """
#     GET or POST Recipes.
#     """
#     if request.method == "GET":
#         allowed_keys = ["id", "name", "number_of_servings"]
        
#         Getter = DataGetterService(RecipeSerializer, Recipe)
        
#         filter_dict, error = Getter.create_filter_dict(
#             input_dict=request.query_params.dict(),
#             allowed_keys=allowed_search_keys
#         )
#         if error:
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
#         result_query = Getter.filterit(filter_dict)
#         serializer = Getter.serialize(result_query)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         Poster = DataPosterService(RecipeSerializer, Recipe)
#         Poster.preprocess_data(request.data)

#         Poster.insert_data()

#         response_data = Poster.construct_response_data()

#         return Response(response_data, status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# @permission_classes([IsDeveloperOrAdmin])
# def ingredients(request):
#     """
#     GET or POST Ingredients.
#     """
#     if request.method == "GET":
#         allowed_search_keys = ["name", "manufacturer"]
        
#         Getter = DataGetterService(IngredientSerializer, Ingredient)
        
#         filter_dict, error = Getter.create_filter_dict(
#             input_dict=request.query_params.dict(),
#             allowed_keys=allowed_search_keys
#         )
#         if error:
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
#         result_query = Getter.filterit(filter_dict)
#         serializer = Getter.serialize(result_query)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         Poster = DataPosterService(IngredientSerializer, Ingredient)
#         Poster.preprocess_data(request.data)

#         Poster.insert_data()

#         response_data = Poster.construct_response_data()

#         return Response(response_data, status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# @permission_classes([IsDeveloperOrAdmin])
# def nutrients(request):
#     """
#     POST Nutrients.
#     """
#     if request.method == "GET":
#         return Response({"message":"Request must be of type POST. Get nutrients through their ingredients."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     if request.method == "POST":
#         Poster = DataPosterService(NutrientSerializer, Nutrients)
#         Poster.preprocess_data(request.data)

#         Poster.insert_data()

#         response_data = Poster.construct_response_data()

#         return Response(response_data, status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# @permission_classes([IsDeveloperOrAdmin])
# def recipeingredients(request):
#     """
#     GET or POST RecipeIngredient.
#     """
#     if request.method == "GET":
#         allowed_search_keys = ["recipe_id", "ingredient_id"]

#         Getter = DataGetterService(RecipeIngredientSerializer, RecipeIngredient)
        
#         filter_dict, error = Getter.create_filter_dict(
#             input_dict=request.query_params.dict(),
#             allowed_keys=allowed_search_keys
#         )
#         if error:
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
#         result_query = Getter.filterit(filter_dict)
#         serializer = Getter.serialize(result_query)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         Poster = DataPosterService(RecipeIngredientSerializer, RecipeIngredient)
        
#         data = Poster.preprocess_data(request.data)
#         Poster.insert_data(data)

#         response_data = Poster.construct_response_data()

#         return Response(response_data, status=status.HTTP_200_OK)
