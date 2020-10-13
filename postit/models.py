from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models



class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    am = models.BigIntegerField(blank=False)
    email = models.EmailField(blank=False)
    github_username = models.CharField(max_length=50, blank=False)
    linkedin_url = models.CharField(max_length=50, blank=False)
    about = models.TextField(blank=False)
    knowledge = models.TextField(blank=False)
    skills = models.TextField(blank=False)
    preferred_teams = models.TextField(blank=False)
    team = models.ForeignKey(Team, blank=True, null=True)
    image_url = models.CharField(max_length=50, blank=False)
