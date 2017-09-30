from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
	"""
	User profile
	"""
	name = models.charField(max_length=100)
	weight = models.IntegerField()
	sessions = models.ManyToOne(sessions)

class Session(models.Model):
	workouts = models.ManyToOne(Workout)

class Excercise(models.Model):
	name = models.charField(max_length=100)
	description = models.charFIeld(max_length=200)

class Workout(models.Model):
	excercise = models.OneToOneField(Excercise)
	sets = models.ManyToOne(Sets)

class Sets(models.Model):
	weight = models.IntegerField()
	sets = models.IntegerField()
	reps = models.IntegerField()





