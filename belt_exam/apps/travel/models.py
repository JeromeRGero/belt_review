# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt
# Create your models here.


class User_Manager(models.Manager):
    def validate_reg(self, pack):
        errors = {}
        checkName = pack['full_name']
        checkUsername = pack['username']
        checkPassword = pack['password']
        checkConfirm =pack['confirm']
        preExisting = User.objects.filter(username=checkName)
        if len(checkName) < 3:
            errors['full_name'] = 'Your entered Name should be at least 3 characters long. ' \
                                  'Travel Manager Co. President and all employees must also have a name' \
                                  ' of at least 3 characters long. '
        if len(preExisting) > 1:
            errors['username'] = "Your username has already been taken! :( sorry... not " + checkUsername + ", Ha ha."
        elif len(checkUsername) < 3:
            errors['username'] = "What are you doing? Your username has to be at least 3 characters long. " \
                                 "I even said so in red text."
        if len(checkPassword) < 8:
            errors['password'] = "Your password needs to be at least 8 characters long. It isn't hard, " \
                                 "you are just stupid."
        if checkPassword != checkConfirm:
            errors['confirm'] = "Oh my god, your fingers must look like all the wires tangled around " \
                                "each other behind your tv set. Try again, I guess."
        # if errors == {}:
        #     password = checkPassword
        #     hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        #     errors['full_name'] = "your hashed password looks like this! {}".format(hashed_pass)
        #     result = bcrypt.checkpw(password.encode(), hashed_pass.encode())
        #     errors['username'] = 'Lets check the result! Here: {}'.format(result)
        return errors

    def validate_log(self, pack):
        error = ""
        checkPassword = pack['password']
        checkUser = pack['username']
        existingUserCheck = User.objects.filter(username=checkUser)
        if len(existingUserCheck) > 0:
            userInfo = User.objects.get(username=checkUser)
            userPass = userInfo.password
            resultPass = bcrypt.checkpw(checkPassword.encode(), userPass.encode())
            if not resultPass:
                error = "Username or Password does not exists or was typed incorrectly."
        else:
            error = "Username or Password does not exists or was typed incorrectly."
        return error


class Travel_Manager(models.Manager):
    def validate_trip(self, pack):
        error = "Your date to leave as either come and gone, or your time to leave from your trip makes no sense!"

        now = datetime.datetime.now()
        now = datetime.datetime.strftime(now, "%Y-%m-%d")
        print(now)
        date_from = pack["date_from"]
        date_to = pack["date_to"]
        date_from = str(date_from)
        date_to = str(date_to)
        print (date_to, date_from)
        print("########################\n{} {} {}\n########################").format(now, date_from, date_to)
        if date_from < date_to:
            if now < date_from:
                print("It works! Fuck you")
                error = ""
                return error
        print("Nope! Still fuck you.")
        return error


class Travel(models.Model):
    creators_name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    desc = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    objects = Travel_Manager()

    def __repr__(self):
        return "\n-----------------------------------\n" \
               "DESTINATION: {}\nDESC: {}\nDATE_FROM: {}\n" \
               "DATE_TO: {}\n-----------------------------------\n" \
               "".format(self.destination, self.desc, self.date_from, self.date_to)


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    travel_plans = models.ManyToManyField(Travel, related_name="users_plans")
    objects = User_Manager()

    def __repr__(self):
        return "\n##########################\n" \
               "NAME: {}\nUSERNAME: {}\nPASSWORD: {}\n" \
               "TRAVEL_PLANS: {}\n##########################\n" \
               "".format(self.name, self.username, self.password, self.travel_plans.all())

