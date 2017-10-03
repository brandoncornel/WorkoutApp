from rest_framework import viewsets
from workouts.models import *
from workouts.serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets, views


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)




class SessionViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Session objects """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
            'status': 'Bad request',
            'message': 'Session could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)




class ExcerciseViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Excercise objects """
    queryset = Excercise.objects.all()
    serializer_class = ExcerciseSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
            'status': 'Bad request',
            'message': 'Excercise could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

class WorkoutViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Workout objects """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
            'status': 'Bad request',
            'message': 'Workout could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

class SetsViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Sets objects """
    queryset = Sets.objects.all()
    serializer_class = SetsSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
            'status': 'Bad request',
            'message': 'Set could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)