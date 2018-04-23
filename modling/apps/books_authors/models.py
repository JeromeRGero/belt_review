# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        # info = self.authors.all()
        # namestr = ""
        # for name in authors:
        #     namestr += name.first_name
        return "\nNAME: {}\nDESC: {}" \
               "\n".format(self.name, self.desc)


class Author(models.Model):
    books = models.ManyToManyField(Book, related_name="authors")
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "\n-----------------------------------------\nBOOKS: {}\nFIRST: {}\nLAST: {}\nEMAIL: {}" \
               "\n".format(self.books.all(), self.first_name, self.last_name, self.email)

