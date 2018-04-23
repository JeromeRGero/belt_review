# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    context = {
        'time': strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print(get_random_string(length=14))
    return render(request, 'clock/index.html', context)
