from rest_framework import viewsets
from workouts.models import *
from workouts.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Session objects """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ExcerciseViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Excercise objects """
    queryset = Excercise.objects.all()
    serializer_class = ExcerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Workout objects """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class SetsViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Sets objects """
    queryset = Sets.objects.all()
    serializer_class = SetsSerializer