from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models



class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    am = models.BigIntegerField(blank=False)
    email = models.EmailField(blank=False)
    github_username = models.CharField(max_length=50, blank=True)
    linkedin_url = models.CharField(max_length=50, blank=True)
    about = models.TextField(blank=False)
    knowledge = models.TextField(blank=False)
    skills = models.TextField(blank=False)
    preferred_teams = models.TextField(blank=True)
    team = models.ForeignKey(Team, blank=True, null=True)
    image_url = models.FileField(blank=False, upload_to='media', null=True)

    @property
    def available(self):
        return self.team is None

    def __unicode__(self):
        return str(self.am) + " (" + self.first_name + " " + self.last_name + ")"

    class Meta:
        ordering = ('am',)
