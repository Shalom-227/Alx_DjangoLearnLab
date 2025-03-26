from django.shortcuts import render
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, TokenSerializer, UserProfileSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView 
from rest_framework.authtoken.views import ObtainAuthToken


# Create your views here.


class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        token_serializer = TokenSerializer(instance=token)
        return Response(token_serializer.data)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()  # Deletes the token upon logout
            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        except (AttributeError, Token.DoesNotExist):
            return Response({"message": "No active token found."}, status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
