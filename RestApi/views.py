from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from RestApi.serializer import UserSerializer,PaymentsSerializer,ShowsSerializer,EpisodeSerializer,HistorySerializer
from .models import Shows, Episode,History,User


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

@api_view(["POST"])
def addBill(request):
    serializer = PaymentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Successful payment"
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCat(request,cat):
    movies = Shows.objects.all().order_by('-publishDate').filter(Categories__name=cat)
    response = ShowsSerializer(instance=movies, many=True)
    return Response(data=response.data, status=status.HTTP_200_OK)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getActor(request,actor):
    movies = Shows.objects.all().order_by('-publishDate').filter(Actors__name=actor)
    response = ShowsSerializer(instance=movies, many=True)
    return Response(data=response.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getEpisodes(request,show,user):
    newHistory=History(user_id=user,show_id=show)
    newHistory.save()
    show_=Shows.objects.get(pk=show)
    if show_:
        show_.views=show_.views+1
        show_.save()
    episodes = Episode.objects.all().order_by('-date').filter(show__id=show)
    response = EpisodeSerializer(instance=episodes, many=True)
    return Response(data=response.data, status=status.HTTP_200_OK)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def likes(request,show):
    show_=Shows.objects.get(pk=show)
    if show_:
        show_.likes=show_.likes+1
        show_.save()
        return Response(data={"success :":True,
                              "Massage":"liked"}, status=status.HTTP_200_OK)
    return Response(data={"success :": False,
                          "Error": "Cant find show"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def disLikes(request,show):
    show_=Shows.objects.get(pk=show)
    if show_:
        show_.disLikes=show_.disLikes+1
        show_.save()
        return Response(data={"success :":True,
                              "Massage":"disliked"}, status=status.HTTP_200_OK)
    return Response(data={"success :": False,
                          "Error": "Cant find show"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getHistory(request,user):
   shows=History.objects.all().order_by("-date").filter(user__id=user)
   response = HistorySerializer(instance=shows, many=True)
   return Response(data=response.data, status=status.HTTP_200_OK)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getId(request,username):
    try:
     user=User.objects.all().filter(username=username)
     return Response(data={"success:":True,
                         "id:":user.pk}, status=status.HTTP_200_OK)
    except NameError:
        return Response(data={"success:": False,
                              "error:": NameError}, status=status.HTTP_400_BAD_REQUEST)