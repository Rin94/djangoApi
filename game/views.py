from sys import api_version

from django.shortcuts import render
from django.http import Http404
from pipenv.patched.pip._vendor.requests.packages.urllib3 import request, request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from game.models import Juego,Desarrolladora
from game.serializers import JuegoSerializer, DesarrolladoraSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class ApiDesarrolladora():

    @api_view(['POST'])
    def create(request):
        serializer= DesarrolladoraSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Desarrolladora Registrada",status=status.HTTP_201_CREATED)
        return Response("No se pudo registrar la wea", status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_all_developers(request):
        queryset=Desarrolladora.objects.all()
        serializer= DesarrolladoraSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @api_view(['GET', 'PUT', 'DELETE'])
    def manage_by_id(request, id):
        if request.method == "GET":
            return ApiDesarrolladora.get_developer_by_id(request,id)
        elif request.method == "DELETE":
            return ApiDesarrolladora.delete_developer(request,id)
        elif request.method == "PUT":
            return ApiDesarrolladora.update_developer(request,id)

    def get_developer_or_response(id):
        try:
            desarrolladora = Desarrolladora.objects.get(id=id)
            return desarrolladora
        except desarrolladora.DoesNotExist:
            return Response("Desarrolladora no identificada, quizas ya quebraron :(", status=status.HTTP_400_BAD_REQUEST)


    def get_developer_by_id(request,id):
        desarrolladora= ApiDesarrolladora.get_developer_or_response(id)

        if isinstance(desarrolladora,Response):
            return desarrolladora
        else:
            desarrolladora= Desarrolladora.objects.get(id=id)
            serializer= DesarrolladoraSerializer(desarrolladora)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def update_developer(request, id):
        desarrolladora = ApiDesarrolladora.get_developer_or_response(id)

        if isinstance(desarrolladora,Response):
            return desarrolladora
        else:
            serializer= DesarrolladoraSerializer(desarrolladora, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Desarrolladora Actualizada", status=status.HTTP_200_OK)
            else:
                return Response("La desarrolladora no se pudo actualizar: "+serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_developer(request, id):
        desarrolladora = ApiDesarrolladora.get_developer_or_response(id)

        if isinstance(desarrolladora,Response):
            return desarrolladora
        else:
            desarrolladora.delete()
            return Response('Desarrolladora eliminada', status=status.HTTP_200_OK)



class ApiJuego():

    @api_view(['POST'])
    def create_game(request):
        serializer =JuegoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Juego Almacenado", status=status.HTTP_201_CREATED)
        else:
            return Response("No se pudo almacenar el juego :( ", status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET'])
    def get_games(request):
        juegos= Juego.objects.all()
        serializer= JuegoSerializer(juegos,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET','PUT','DELETE'])
    def manage_game_by_id(request,id):
        if request.method=="GET":
            return ApiJuego.get_game(request,id)
        elif request.method=="PUT":
            return  ApiJuego.update_game(request,id)
        elif request.method=="DELETE":
            return ApiJuego.delete_game(request,id)

    def get_game_or_response(request,id):
        try:
            juego = Juego.objects.get(id=id)
            return juego
        except juego.DoesNotExist:
            return Response("Juego no existe o es japones :(", status=status.HTTP_400_BAD_REQUEST)


    def get_game(request,id):

        juego=ApiJuego.get_game_or_response(request,id)
        if isinstance(juego, Response):
            return juego
        else:
            serializer = JuegoSerializer(juego)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def update_game(request, id):

        juego = ApiJuego.get_game_or_response(request,id)
        if isinstance(juego, Response):
            return juego
        else:
            serializer = JuegoSerializer(juego,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Juego Actualizado Papu", status=status.HTTP_200_OK)
            else:
                return Response("No se pudo actualizar el juego :( ", status=status.HTTP_400_BAD_REQUEST)



    def delete_game(request, id):
        juego = ApiJuego.get_game_or_response(request,id)
        if isinstance(juego, Response):
            return juego
        else:
            juego.delete()
            return Response("Juego eliminado", status=status.HTTP_200_OK)

class ApiJuegos2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset= Juego.objects.all()
    serializer_class= JuegoSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)









