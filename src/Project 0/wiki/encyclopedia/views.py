from django.shortcuts import render
import os
from . import util

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def content(request, word):
    entries_lst = os.listdir('entries')
    md_word = word + '.md'
    if (md_word in entries_lst):
        print("css.md is in here")
    return render(request, 'encyclopedia/content.html', {
        'word': word
    })