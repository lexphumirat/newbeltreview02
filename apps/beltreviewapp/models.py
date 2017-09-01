# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models
from django.contrib import messages

# Create your models here.
class UserManger(models.Manager):
    #send info over to views def register
    def validate_reg(self, post_data):
        errors = []
        # email exist
        if self.filter(email=post_data['email']):
            errors.append('email exist already')
        #username and alias must be 2 or more
        if len(post_data['full_name']) < 2:
            errors.append('username must be 2 or more characters')
        if len(post_data['alias']) < 2:
            errors.append('alias must be 2 or more characters')
        #password must be 8 or more
        #password must be the same as confirm
        if len(post_data['password']) < 8:
            errors.append('password must be 8 or more characters')
        if len(post_data['password']) != len(post_data['confirmpw']):
            errors.append('password must match')
        return errors

    def validate_login(self, post_data):
        #email is not in system
        errors = []
        the_user = None
        if not self.filter(email=post_data['email']):
            errors.append('incorrect email or password')
        else:
            the_user = self.get(email=post_data['email'])
            if bcrypt.checkpw(post_data['password'].encode(), the_user.password.encode()):
                errors.append('incorrect email or password')
                the_user = None
                #password is incorrect

        return (errors, the_user)

    def create_user(self, clean_data):
        hashed = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            full_name = clean_data['full_name'],
            alias = clean_data['alias'],
            email = clean_data['email'],
            password = hashed,
            dob = clean_data['dob']
        )


class User(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    alias = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManger()

    def __str__(self):
        return self.full_name + " " + self.email
