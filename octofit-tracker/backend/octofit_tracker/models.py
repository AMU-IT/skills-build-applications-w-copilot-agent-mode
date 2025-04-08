from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)  # Store user ObjectId references as a JSON array

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {this.points} points"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name
