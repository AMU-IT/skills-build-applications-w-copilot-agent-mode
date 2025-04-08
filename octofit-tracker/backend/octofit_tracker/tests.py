from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2025-04-08")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Test Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session", duration=60)
        self.assertEqual(workout.name, "Morning Yoga")
