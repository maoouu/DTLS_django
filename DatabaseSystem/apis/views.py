from django.contrib.auth import login, logout
from django.shortcuts import render

from rest_framework import viewsets, generics, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.status import HTTP_200_OK

from .serializers import RecordSerializer, UserSerializer, RegisterSerializer
from EnvergaDB.models import Records


# Record API
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RecordSerializer


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return super(LoginAPI, self).post(request, format=None)


# Logout API
class LogoutAPI(KnoxLogoutView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        super(LogoutAPI, self).post(request, format=None)

        return Response({"success": "User logged out successfully."})


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            #"user": UserSerializer(user, context=self.get_serializer_context()).data,
            #"token": AuthToken.objects.create(user)[1],
            "success": "A new user has been registered."
        })