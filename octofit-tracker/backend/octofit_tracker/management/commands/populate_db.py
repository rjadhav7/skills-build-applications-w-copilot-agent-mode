
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users (Superheroes)
        users = [
            User(email='tony@stark.com', username='IronMan', team=marvel),
            User(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User(email='bruce@wayne.com', username='Batman', team=dc),
            User(email='clark@kent.com', username='Superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Create Activities
        activities = [
            Activity(user=users[0], type='run', duration=30, points=50),
            Activity(user=users[1], type='walk', duration=60, points=40),
            Activity(user=users[2], type='strength', duration=45, points=60),
            Activity(user=users[3], type='run', duration=20, points=30),
        ]
        Activity.objects.bulk_create(activities)

        # Create Workouts
        workouts = [
            Workout(user=users[0], name='Morning Cardio', description='5km run'),
            Workout(user=users[2], name='Night Strength', description='Pushups and pullups'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=90)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

        # Unique index on email is enforced by Django model
