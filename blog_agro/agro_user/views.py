from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status, generics, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from agro_user.models import AgroUser
from agro_user.serializers import RegisterSerializer, LoginSerializer, AgroUserSearchSerializer
from rest_framework.permissions import *
from agro_user.permissions import *
from drf_yasg.utils import swagger_auto_schema


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={
           'message': 'good',
           'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            email=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'User not found or does not exist'})
        else:
            token = Token.objects.get_or_create(user=user)
            return Response(data={'token': str(token)},
                            status=status.HTTP_200_OK)



class AgroUserSearchView(generics.ListAPIView):
    queryset = AgroUser.objects.all()
    serializer_class = AgroUserSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']