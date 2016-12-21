from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag

# Create your models here.
class Bloggg(models.Model):
    title = models.CharField(max_length=250)
    parag = models.CharField(max_length=250)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)