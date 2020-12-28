from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
import markdown2
from . import util
from .forms import SearchForm
import random

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def content(request, word):
    entries_lst = util.list_entries()
    entries_lst_lower = [i.lower() for i in entries_lst]
    if (word.lower() not in entries_lst_lower):
        raise Http404("Wiki entry does not exist.")
    
    with open(f'entries/{word}.md', 'r') as f:
        markdown_content = f.read()

    markdown_to_html = markdown2.markdown(markdown_content)
    with open('encyclopedia/templates/encyclopedia/filter.html', 'w') as f:
        f.write(markdown_to_html)
    
    return render(request, 'encyclopedia/content.html', {
        'word': word
    })

def get_search(request):

    if request.method == 'GET':
        #form = SearchForm(request.GET)
        data = request.GET
        query = data['q']

        entries_lst = util.list_entries()

        return HttpResponseRedirect('/wiki/' + query)
    
def random_page(request):

    word = random.choice(util.list_entries())

    with open(f'entries/{word}.md', 'r') as f:
        markdown_content = f.read()

    markdown_to_html = markdown2.markdown(markdown_content)
    with open('encyclopedia/templates/encyclopedia/filter.html', 'w') as f:
        f.write(markdown_to_html)

    return render(request, 'encyclopedia/content.html', {
        'word': word
    })   