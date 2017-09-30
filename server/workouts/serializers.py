from rest_framework import serializers
from workouts.models import *

class UserSerializer(models.Model):
	class Meta:
		model = User
		fields = ("name", "weight")

class SessionSerializer(models.Model):
	class Meta:
		model = Session
		fields = ("date", "user")

class ExcerciseSerializer(models.Model):
	class Meta:
		model = Excercise
		fields = ("name", "description")

class WorkoutSerializer(models.Model):
	class Meta:
		model = Workout
		fields = ("session", "excercise")

class SetsSerializer(models.Model):
	class Meta:
		model = Sets
		fields = ("workout", "weight", "sets", "reps")