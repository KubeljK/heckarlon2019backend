from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status, permissions, generics, mixins
from rest_framework.response import Response

from apps.userprofile.serializers import UserSerializer, UserRegisterSerializer, ProfileSerializer
from apps.userprofile.permissions import OwnProfilePermission
from apps.userprofile.models import Profile


class RegisterUsers(generics.CreateAPIView):
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

    permission_classes = (permissions.IsAdminUser, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveAPIView):

    permission_classes = (permissions.IsAdminUser, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

class EditProfile(generics.RetrieveUpdateAPIView):

    permission_classes = (OwnProfilePermission, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj
