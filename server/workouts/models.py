from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
	"""
	User profile
	"""
	name = models.CharField(max_length=100)
	weight = models.IntegerField()

class Session(models.Model):
	date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User)

class Excercise(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)

class Workout(models.Model):
	session = models.ForeignKey(Session)
	excercise = models.OneToOneField(Excercise)

class Sets(models.Model):
	workout = models.ForeignKey(Workout)
	weight = models.IntegerField()
	sets = models.IntegerField()
	reps = models.IntegerField()





