from django.shortcuts import render
from django.http import HttpResponse
import os
import markdown2
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
    
    content_html = """<div> <h1>heading</h1> </div>
    <p>CSS is cook</p>
    """
    with open('encyclopedia/templates/encyclopedia/filter.html', 'w') as f:
        #src\Project 0\wiki\encyclopedia\templates\encyclopedia\filter.html
        f.write(content_html)
    
    return render(request, 'encyclopedia/content.html', {
        'word': word
    })