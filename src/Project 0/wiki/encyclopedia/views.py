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
    # if (md_word in entries_lst):
    #     print("css.md is in here")
    
    with open(f'entries/{md_word}', 'r') as f:
        content = f.read()

    markdown_to_html = markdown2.markdown(content)
    with open('encyclopedia/templates/encyclopedia/filter.html', 'w') as f:
        f.write(markdown_to_html)
    
    return render(request, 'encyclopedia/content.html', {
        'word': word
    })