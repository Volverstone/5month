from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from users.serializers import UserClassSerializer, UserAuthSerializer
from django.contrib.auth import authenticate

@api_view(['POST'])
def authorization_user_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key':token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST'])
def registration_api_view(request):
    serializer = UserClassSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)


    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(username=username,
                                    password=password,
                                    is_active=True)

    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id':user.id})
