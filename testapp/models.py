# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField(blank=False, null=False)
#     password = models.CharField(blank=False, null=False)

class Message(models.Model):
    title= models.CharField(blank=False, null=False, max_length=50)
    explanation= models.TextField(blank=False, null=False, max_length=280)