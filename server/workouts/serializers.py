from rest_framework import serializers
from workouts.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("name", "weight")

class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = ("date", "user")

class ExcerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Excercise
		fields = ("name", "description")

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ("session", "excercise")

class SetsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sets
		fields = ("workout", "weight", "sets", "reps")