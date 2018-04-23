# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Dojos(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)

    def __repr__(self):
        return "\nNAME: {} \nCITY: {} \nSTATE: {} DESCRIPTION: {}" \
               "\n".format(self.name, self.city, self.state, self.desc)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __repr__(self):
        return "\nDOJO: {} \nFIRST: {} \nLAST: {}" \
               "\n".format(self.dojo.city, self.first_name, self.last_name)
