# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.


def index(request):
    a = 'Hello?'
    # return HttpResponse(a)
    return render(request, "reg_log/index.html")

def register(request):
    errors = {}
    request.session['errors'] = {}
    if request.POST:
        errors = User.objects.validate_reg(request.POST)
        print(errors)
        if len(errors):
            request.session['errors'] = {}
            for i in errors:
                request.session['errors'][i] = errors[i]
            return redirect('/')
        else:
            # firstF = request.POST['first_name']
            # lastF = request.POST['last_name']
            # emailF = request.POST['email']
            # passF = request.POST['password']
            # User.objects.create(first_name=firstF, last_name=lastF, email=emailF, password=passF)
            return redirect('/')
    # b = 'I promise I\'m working!'

    return redirect('/')

def login(request):
    c = 'What are you doing?'
    return HttpResponse(c)
