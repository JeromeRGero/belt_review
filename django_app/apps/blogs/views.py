# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from django.shortcuts import render

# Create your views here.

def index(request):
    response = "Must make index... ndex... dex... edex... kedex... okedex... pokedex..."
    return HttpResponse(response)


def newblog(request):
    response1 = "placeholder to display a new form to create a new blog"
    return HttpResponse(response1)


def show(request, num):
    response = "placeholder to display blog {}".format(num)
    return HttpResponse(response)

def edit(request, num):
    response = "placeholder to edit blog {}".format(num)
    return HttpResponse(response)


def destroy(request, num):
    return redirect('/')
