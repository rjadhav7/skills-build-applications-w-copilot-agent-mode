from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('run', 'Run'),
        ('walk', 'Walk'),
        ('strength', 'Strength'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    points = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.team.name}: {self.points} points"
