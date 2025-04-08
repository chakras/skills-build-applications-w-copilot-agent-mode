from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

# Ensure the Command class is properly defined
class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Connecting to MongoDB...')
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        self.stdout.write('Dropping existing collections...')
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        self.stdout.write('Inserting users...')
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)
        self.stdout.write(f'Inserted {len(users)} users.')

        self.stdout.write('Inserting teams...')
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"], users[2]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)
        self.stdout.write(f'Inserted {len(teams)} teams.')

        self.stdout.write('Inserting activities...')
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 3600},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 7200},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 5400},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 1800},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 4500},
        ]
        db.activity.insert_many(activities)
        self.stdout.write(f'Inserted {len(activities)} activities.')

        self.stdout.write('Inserting leaderboard entries...')
        leaderboard_entries = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard_entries)
        self.stdout.write(f'Inserted {len(leaderboard_entries)} leaderboard entries.')

        self.stdout.write('Inserting workouts...')
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)
        self.stdout.write(f'Inserted {len(workouts)} workouts.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
