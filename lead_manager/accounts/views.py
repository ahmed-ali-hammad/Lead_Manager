from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from knox.models import AuthToken
from .serializers import *


# Registeration API
class UserRegisterAPIView (APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            user = serializer.save()
            token = AuthToken.objects.create(user)
        else: 
            return Response({
                "Message": "Invalid Credential"
            }, status = status.HTTP_400_BAD_REQUEST)
        return Response({
            "user": serializer.data,
            "token" : token[1]
        })


# Login API
class UserLoginAPIView(APIView): 
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username = username, password=password)

        if user is not None:
            token_object = AuthToken.objects.create(user)
            token = token_object[1]
            return Response({
                    "user":{
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    },
                    "token": token
                })
        else: 
            return Response ({"message": "User dosn't exist"}, status = status.HTTP_404_NOT_FOUND)


# user detail API
class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserDetailSerializer
    
    def get_object(self):
        return self.request.user