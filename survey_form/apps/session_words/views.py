# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return render(request, 'session_words/index.html')

def add(request):
    if 'ppack' not in request.session:
        request.session['ppack'] = []
    word = request.POST.get('word', 'FAIL')
    color = request.POST.get('color', 'FAIL')
    big = '14px'
    if request.POST.get('big', False):
        big = '30px'

    request.session['ppack'].append(
        {
            'word': word,
            'color': color,
            'size': big,
        }
    )
    print request.session['ppack']
    request.session.modified=True
    return redirect('/session_words')


def clear(request):
    request.session['ppack'] = []
    request.session.modified=True
    return redirect('/session_words')