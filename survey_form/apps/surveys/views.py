# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def index(request):
    if "count" not in request.session:
        request.session['count'] = 0
    return render(request, 'surveys/index.html')


def submit(request):
    request.session['pack'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'lang':  request.POST['lang'],
        'comment': request.POST['comment'],
    }
    print(request.session['pack']['name'])
    return redirect('/result')


def result(request):
    request.session['count'] += 1
    return render(request, "surveys/result.html")
