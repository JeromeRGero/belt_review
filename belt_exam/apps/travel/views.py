# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Travel
import bcrypt
import datetime

# Create your views here.


def index(request):
    return render(request, "travel/index.html")


def travelspage(request):

    thierID = request.session['id']
    travel_plans = Travel.objects.filter(users_plans=thierID)
    request.session['usertrips'] = travel_plans

    request.session.modified = True
    print(request.session['name'])
    # context = {
    #     'users': u
    # }
    # travelplans = user.travel_plans
    # request.session['usertrips'] = trips
    # Travel.objects.exclude(users_plans=travelplans)
    return render(request, "travel/travels.html")


def addtrippage(request):
    c = "I promis I am functional!"
    return render(request, "travel/add.html")


def destinationpage(request, num):
    d = "Working! Number {}! Please leave now!".format(num)
    return HttpResponse(d)


def login(request):
    if "loghold" in request.session:
        pulledUsername = request.session["loghold"]["username"]
        print(pulledUsername.name)
        user = User.objects.get(username=pulledUsername)
        for key in request.session.keys():
            del request.session[key]
        request.session = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
        }
        request.session.modified = True
        return redirect('/travels')
    elif request.POST:
        error = User.objects.validate_log(request.POST)
        if len(error) > 0:
            print("You have ERRORS!!!!!!")
            request.session['LOGerror'] = error
            return redirect("/main")
        else:
            print('No errors~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            username = request.POST['username']
            userObj = User.objects.get(username=username)
            print(userObj.name)
            thierID = userObj.id
            thierUN = userObj.username
            thierNA = userObj.name
            request.session['ID'] = thierID
            request.session['']
            return redirect('/travels')
    print("Shit, why is this printing?")
    return redirect('/main')


def reg(request):
    errors = User.objects.validate_reg(request.POST)
    print(errors)
    if len(errors) > 0:
        request.session['errors'] = {}
        for i in errors:
            request.session['errors'][i] = errors[i]
        request.session.modified = True
        return redirect('/')
    else:
        firstF = request.POST['full_name']
        lastF = request.POST['username']
        passF = request.POST['password']
        passHashed = bcrypt.hashpw(passF.encode(), bcrypt.gensalt())
        print(firstF, lastF, passF)
        User.objects.create(name=firstF, username=lastF, password=passHashed)
        for key in request.session.keys():
            del request.session[key]
        request.session['loghold'] = {
            "username": lastF,
            "password": passHashed
        }
        return redirect('/login')


def logout(request):
    for key in request.session.keys():
        del request.session[key]
    request.session.modified=True
    return redirect('/main')


def forOfor(request):
    z = "AHHHHHHHHHHHHHH!!!!"
    return HttpResponse(z)


def adding(request):
    if request.POST:
        print(request.POST)
        errors = Travel.objects.validate_trip(request.POST)
        if len(errors) < 1:
            name = request.session['name']
            destin = request.POST['destination']
            desc = request.POST['desc']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            date_from = str(date_from)
            date_to = str(date_to)
            # date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d")
            # date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d")
            print(name, destin, desc, date_from, date_to)
            newplan = Travel.objects.create(creators_name=name, destination=destin, desc=desc, date_from=date_from, date_to=date_to)
            User.objects.get(name=name).travel_plans.add(newplan)
            request.session['error'] = ""
            request.session.modified = True
            return redirect('/travels')
        else:
            request.session['error'] = errors
            request.session.modified = True
            return redirect('/travels/add')
    return HttpResponse("Hello?")