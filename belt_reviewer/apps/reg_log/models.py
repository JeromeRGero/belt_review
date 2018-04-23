# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
# Create your models here.


class Reg_Log_Manager(models.Manager):

    def validate_reg(self, pack):
        errors = {}
        if len(pack['first_name']) > 50:
            errors['first_name'] = 'Your entered first name should only be a max of 50 characters long!'
        if len(pack['last_name']) > 50:
            errors['last_name'] = 'Your entered last name should only be a max of 50 characters long!'

        if ".com" not in pack['email']:
            errors['email'] = 'You need to include a .com in your email!'
        if len(pack['password']) < 8:
            errors['password'] = "Your password needs to be at least 8 characters!"

        print(pack['password'])
        print(pack['confirm'])
        if pack['password'] != pack['confirm']:
            errors['confirm'] = "Your passwords didn't match... sorry :("
        if errors == {}:
            fname= pack['first_name']
            lname= pack['last_name']
            email= pack['email']
            password = pack['password']
            hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())


            User.objects.create()
        return errors

    def validate_log(self, pack):
        errors = {}
        if pack:
            print('You did it!')
        else:
            print("Why did you fail?")
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = Reg_Log_Manager()

    def __repr__(self):
        return "\n---------------------\n" \
               "USER's NAME: {} {}\nEMAIL:{}\nPASSWORD: {}" \
               "\n---------------------\n".format(self.first_name, self.last_name, self.email, self.password)
