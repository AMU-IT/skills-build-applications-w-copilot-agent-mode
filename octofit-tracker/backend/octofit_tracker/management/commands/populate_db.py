from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        blue_team.save()
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        gold_team.save()

        # Adding members to teams by storing user IDs
        blue_team.members = [user._id for user in users[:3]]  # First three users to Blue Team
        blue_team.save()

        gold_team.members = [user._id for user in users[3:]]  # Remaining users to Gold Team
        gold_team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=blue_team, points=100),
            Leaderboard(_id=ObjectId(), team=gold_team, points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
