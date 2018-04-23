# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=120)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "first {} \nlast {} \nemail {} \nage {} \ncreated {} \nupdate " \
               "{}".format(self.first_name, self.last_name, self.email, self.age, self.created_at, self.updated_at)

