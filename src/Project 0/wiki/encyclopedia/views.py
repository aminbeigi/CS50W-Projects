from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
import markdown2
from . import util
from .forms import EntryForm
import random
from django.contrib import messages

# TODO: urls should match exact or lowercase

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
        data = request.GET
        query = data['q']

        entries_lst = util.list_entries()
        entries_lst_lower = [i.lower() for i in entries_lst]
        if (query.lower() in entries_lst_lower):
            return HttpResponseRedirect('/wiki/' + query)   
       
        substring_search_lst = []

        for entry in entries_lst:
            if query.lower() in entry.lower():
                substring_search_lst.append(entry)

        # if len(substring_search_lst) == 0:
        #     raise Http404("Wiki entry does not exist.")

        return render(request, 'encyclopedia/search_query.html', {
            'entry_lst': substring_search_lst,
            'query': query
        })

    
def random_page(request):
    word = random.choice(util.list_entries())
    return HttpResponseRedirect('/wiki/' + word)

def create_new_page(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')

            entries_lst_lower = [i.lower() for i in util.list_entries()]
            if title.lower() in entries_lst_lower:
                messages.error(request, f"Error: {title} already exists.")
                return redirect(create_new_page)            
            
            content = form.cleaned_data.get('content')
            messages.success(request, f"Success: {title} entry created.")
            util.save_entry(title, content)
            return redirect('/wiki/' + title)
    else:
        form = EntryForm()
    return render(request, 'encyclopedia/create_new_page.html', {
        'form': form
    })

def edit_entry(request, word):
    form = EntryForm()
    return render(request, 'encyclopedia/edit_entry.html', {
        'word': word
    })