# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.

class User_Manager(models.Manager):
    def validate_reg(self, pack):
        errors = []
        checkName = pack['full_name']
        checkAlias = pack['alias']
        checkEmail = pack['email']
        checkPassword = pack['password']
        checkConfirm = pack['confirm']
        preExisting = User.objects.filter(email=checkEmail)
        if len(checkName) < 2:
            errors.append('Your nane must be at least 2 characters long.')
        if len(checkAlias) > 25:
            errors.append("The length of your alias is far to large!")
        if len(preExisting) > 0:
            errors.append("Your email has already been taken! :( sorry... not " + checkEmail + ", Ah-ha.")
        elif '.com' not in checkEmail:
            errors.append("What are you doing? Your email has to have a .com or .org. It is almost as if you don't care!")
        if len(checkPassword) < 8:
            errors.append("Your password needs to be at least 8 characters long. It isn't hard, " \
                                 "you are just stupid.")
        if checkPassword != checkConfirm:
            errors.append("Oh my god. Your fingers must look like all the wires behind your tv set. " \
                                "So first, untangle yourself. Then try again.")
        print ('I am running!')
        # if errors == []:
        #     hashed_pass = bcrypt.hashpw(checkPassword.encode(), bcrypt.gensalt())
        #     errors.append("your hashed password looks like this! {}".format(hashed_pass))
        #     result = bcrypt.checkpw(checkPassword.encode(), hashed_pass.encode())
        #     errors.append('Lets check the result! Here: {}'.format(result))
        # (Except for now...) this can return an empty dict, or one filled with error messages.
        return errors

    def validate_log(self, pack):
        print('The login validator has been hit!')
        error = "Username or Password does not exists or was typed incorrectly."
        checkEmail = pack['email']
        checkEmail = checkEmail.lower()
        print("You typed in {} as your email.".format(checkEmail))
        checkPassword = pack['password']
        existingUserCheck = User.objects.filter(email=checkEmail)
        print("Length of existing user search is: {}".format(len(existingUserCheck)))
        if len(existingUserCheck) > 0:
            userPass = User.objects.get(email=checkEmail).hashedPassword
            resultPass = bcrypt.checkpw(checkPassword.encode(), userPass.encode())
            print(resultPass)
            if resultPass:
                error = ""
                return error
        # returns error as a string * I-F * errors exist.
        return error


class Book_Manager(models.Model):
    def validate_book(self, title):
        existing = Book.objects.filter(title=title)
        if len(existing) > 0:
            existing = False
        else:
            existing = True
        return existing

class Author_Manager(models.Model):
    def validate_auth(self, name):
        existing = Author.objects.filter(name=name)
        if len(existing) > 0:
            existing = False
        else:
            existing = True
        return existing

class Author(models.Model):
    name = models.CharField(max_length=255)
    objects = Author_Manager()

    def __repr__(self):
        return "\n##########################\n" \
               "NAME: {}\n##########################\n".format(self.name)


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField()
    hashedPassword = models.CharField(max_length=255)
    objects = User_Manager()

    def __repr__(self):
        return "\n##########################\n" \
               "NAME: {}\nALIAS: {}\nEMAIL: {}\n" \
               "HASHED-PASSWORD: {}\n##########################\n" \
               "".format(self.name, self.alias, self.email, self.hashedPassword)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    objects = Book_Manager()

    def __repr__(self):
        return "\n##########################\n" \
               "TITLE: {}\nAUTHOR: {}\n##########################\n".format(self.title, self.author.name)


class Reviews(models.Model):
    review = models.TextField()
    stars = models.IntegerField()
    user = models.ForeignKey(User, related_name="user_reviews")
    book = models.ForeignKey(Book, related_name="book_reviews")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "\n##########################\n" \
               "REVIEW: {}\nBOOK: {}\nSTARS: {}\n" \
               "##########################\n".format(self.review, self.book.title, self.stars)
