# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Reviews, Book, Author
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def reg(request):
    if request.POST:
        errors = User.objects.validate_reg(request.POST)
        if len(errors) > 0:
            user_errors = ""
            for error in errors:
                user_errors += error + " \n"
            request.session['reg_errors'] = user_errors
            # for tag, error in errors.itteritems():
            #     print (tag, error)
            #     messages.error(request, error, extra_tags=tag)
            return redirect('/')
        if 'reg_errors' in request.session.keys():
            del request.session['reg_errors']
        name = request.POST['full_name']
        alias = request.POST['alias']
        email = request.POST['email']
        email = email.lower()
        NOTHASHED = request.POST['password']
        hashedPassword = bcrypt.hashpw(NOTHASHED.encode(), bcrypt.gensalt())
        User.objects.create(name=name, alias=alias, email=email, hashedPassword=hashedPassword)
        userid = User.objects.get(email=email).id
        print(userid)
        request.session['userid'] = int(userid)
    return redirect('/books')


def login(request):
    if request.POST:
        error = User.objects.validate_log(request.POST)
        if len(error) > 0:
            print("There was an error during login,")
            print(error)
            request.session['log_error'] = error
            # for tag, error in errors.itteritems():
            #     print (tag, error)
            #     messages.error(request, error, extra_tags=tag)
            return redirect('/')
        if 'log_error' in request.session.keys():
            del request.session['log_error']
        email = request.POST['email']
        email = email.lower()
        userObj = User.objects.get(email=email)
        userid = userObj.id
        print(userid)
        request.session['userid'] = userid
        return redirect('/books')
    print("No request.POST found... huh?")
    return redirect('/')


def logout(request):
    del request.session['userid']
    return redirect('/')


def books(request):
    if 'userid' in request.session.keys():
        userid = request.session['userid']
        print(userid)
        users_reviews = User.objects.get(id=userid).user_reviews.order_by("-id")
        print(users_reviews)
        this_user_obj = User.objects.get(id=userid)
        username = this_user_obj.name
        not_this_users_reviews = Reviews.objects.exclude(user=this_user_obj)
        context = {
            'this_users_reviews': users_reviews,
            'not_this_users_reviews': not_this_users_reviews,
            'name': username,
            'userid': userid,
        }
        return render(request, 'main/books.html', context)
    else:
        a = 'Not logged in yet! Visit the main page to login.'
        return HttpResponse(a)


def addpage(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'main/add.html', context)


def adding(request):
    if request.POST:
        title = request.POST['title']
        new_author_name = ""
        if request.POST['new_author'] == "":
            print("The Author textfield should be emty.")
            existing_author_id = int(request.POST['author'])
            authorObj = Author.objects.get(id=existing_author_id)
        else:
            print('There should be a new author\'s name next line!')
            new_author_name = request.POST['new_author']
            Author.objects.create(name=new_author_name)
            authorObj = Author.objects.get(name=new_author_name)
        Book.objects.create(title=title, author=authorObj)
        the_book = Book.objects.get(title=title)
        userid = request.session['userid']
        userObj = User.objects.get(id=userid)
        review = request.POST['review']
        stars = request.POST['rating']
        Reviews.objects.create(review=review, stars=stars, user=userObj, book=the_book)
    return redirect('/books')