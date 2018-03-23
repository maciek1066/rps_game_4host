from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View
from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer
# Create your views here.


class MoviesView(APIView):
    def get_object(self):
        try:
            movies = Movie.objects.all()
        except Movie.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,
                                     context={"request": request},
                                     many=True)
        return Response(serializer.data)


class MovieView(APIView):

    def get_object(self, id):
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie,
                                     context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie,
                                     data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


#Viewsety
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_fields = ('title', 'year')
    ordering_fields = 'title'


