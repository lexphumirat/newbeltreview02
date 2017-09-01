# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib import messages

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    alias = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name + " " + self.email
