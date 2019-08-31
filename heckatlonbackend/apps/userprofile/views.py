from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status, permissions, generics, mixins
from rest_framework.response import Response

from apps.userprofile.serializers import UserSerializer, UserRegisterSerializer,\
    ProfileSerializer, InventorySerializer, InventoryIngredientInsertSerializer,\
    InventoryListSerializer, InventoryIngredientUpdateSerializer
from apps.userprofile.permissions import OwnProfilePermission
from apps.userprofile.models import Profile, Inventory, InventoryIngredient


class RegisterUsers(generics.CreateAPIView):
    """
    Register a new User.
    POST method.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()

        return Response(
            data={
                "message": "User created",
                "user": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

class UsersList(generics.ListAPIView):
    """
    Lists all Users.
    GET method.
    """

    permission_classes = (permissions.IsAdminUser, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve or specific User-Profile object.
    GET method.
    """

    permission_classes = (permissions.IsAdminUser, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

class EditProfile(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a User-Profile object.
    Based on request.user object.
    GET, PATCH and PUT methods.
    """

    permission_classes = (OwnProfilePermission, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

class InventoryList(generics.ListAPIView):
    """
    List all Inventory objects.
    GET method.
    """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = InventoryListSerializer
    queryset = Inventory.objects.all()

    pagination_class = None

    def get_queryset(self):
        queryset = Inventory.objects.filter(user=self.request.user)
        return queryset

class InventoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or Update an Inventory object.
    Can also insert new Inventory-Ingredient objects.
    GET, PUT, PATCH and POST methods.
    """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

    def post(self, request, *args, **kwargs):
        # Get Inventory object directly from request.
        data = request.data
        data["inventory_id"] = self.get_object().id

        serializer = InventoryIngredientInsertSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

class InventoryIngredientUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or Update an Inventory-Ingredient object.
    GET, PUT and PATCH methods.
    """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = InventoryIngredientUpdateSerializer
    queryset = InventoryIngredient.objects.all()
