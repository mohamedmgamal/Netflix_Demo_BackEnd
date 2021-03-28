from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from RestApi.serializer import UserSerializer


@api_view(["POST"])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "New user added successfully "
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    token = Token.objects.all().filter(key=request.data.get('token'))
    try:
        token.delete()
        return Response(data={
            "message": "logout successfully"
            }, status=status.HTTP_200_OK)
    except Exception:
        return Response(data={
                    "Error": Exception
                }, status=status.HTTP_400_BAD_REQUEST)