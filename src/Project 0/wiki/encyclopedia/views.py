from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
import markdown2
from . import util
from .forms import SearchForm

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def content(request, word):
    entries_lst = os.listdir('entries')
    markdown_file = word + '.md'
    if (markdown_file not in entries_lst):
        raise Http404("Wiki entry does not exist.")
    
    with open(f'entries/{markdown_file}', 'r') as f:
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
        print('#'*12, data['q'])
        return HttpResponseRedirect('/')