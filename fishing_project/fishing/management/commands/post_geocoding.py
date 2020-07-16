from django.core.management.base import BaseCommand
import json
from django.contrib.auth.models import User
from django.db import models
import requests
from fishing.models import Post
from fishing import secrets


# https://developers.google.com/maps/documentation/geocoding/start

class Command(BaseCommand):
    def handle(self, *args, **options):

        for post in Post.objects.all():
            print('hello!!!!!!!!!!!!!!!')
            print(post)
            if post.latitude != 0 or post.longitude != 0:
                continue
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            response = requests.get(url, params={
                'address': post.location,
                'key': secrets.google_api_key
            })
            data = response.json()
            location = data['results'][0]['geometry']['location']
            print(location)
            print(post)
            post.latitude = location['lat']
            post.longitude = location['lng']
            post.save()

            

        # for post in Post.objects.all():
