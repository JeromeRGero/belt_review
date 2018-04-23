# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    rando_stringo = get_random_string(length=14)
    context = {
        "random": rando_stringo
    }
    return render(request, 'random_word/index.html', context)


def reset(request):
    if request.method == "POST":
        print(request.POST)
    print(request.POST['reset'])
    request.session['counter'] += 1
    return redirect('/random_words')

