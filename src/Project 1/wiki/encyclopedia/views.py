from django.shortcuts import render, redirect
from django.http import Http404
import os
import markdown2
from . import util
from .forms import EntryForm, EditEntryForm
import random
from django.contrib import messages

VALID_FIRST_CHAR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def content(request, title):
    print(title)
    entries_lst = util.list_entries()
    entries_lst_lower = [i.lower() for i in entries_lst]

    # urls should match exactcase or lowercase
    if title.lower() not in entries_lst_lower:
        raise Http404("Wiki entry does not exist.")

    print(title)

    if title not in entries_lst and title not in entries_lst_lower:
        raise Http404("Wiki entry does not exist.")

    with open(f'entries/{title}.md', 'r') as f:
        markdown_content = f.read()

    markdown_to_html = markdown2.markdown(markdown_content)
    with open('encyclopedia/templates/encyclopedia/filter.html', 'w') as f:
        f.write(markdown_to_html)
    
    return render(request, 'encyclopedia/content.html', {
        'title': title
    })

def get_search(request):
    if request.method == 'GET':
        data = request.GET
        query = data['q']

        entries_lst = util.list_entries()
        entries_lst_lower = [i.lower() for i in entries_lst]
        if (query.lower() in entries_lst_lower):
            return redirect('/wiki/' + query)   
       
        substring_search_lst = []

        for entry in entries_lst:
            if query.lower() in entry.lower():
                substring_search_lst.append(entry)

        return render(request, 'encyclopedia/search_query.html', {
            'entry_lst': substring_search_lst,
            'query': query
        })

    
def random_page(request):
    title = random.choice(util.list_entries())
    return redirect('/wiki/' + title)

def create_new_page(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            
            title = form.cleaned_data.get('title')
            
            if title[0] not in VALID_FIRST_CHAR:
                messages.error(request, f"{title} can not begin with a special character.")
                return redirect(create_new_page)            

            entries_lst_lower = [i.lower() for i in util.list_entries()]
            if title.lower() in entries_lst_lower:
                messages.error(request, f"{title} already exists.")
                return redirect(create_new_page)            
            
            content = form.cleaned_data.get('content')
            messages.success(request, f"{title} entry created.")
            util.save_entry(title, content)
            return redirect('/wiki/' + title)
    else:
        form = EntryForm()
    return render(request, 'encyclopedia/create_new_page.html', {
        'form': form
    })

def edit_entry(request, title):
    with open(f'entries/{title}.md', 'r', newline='\r\n') as f:
       page_content = f.read().replace('\r', '')

    form = EditEntryForm(initial={'title': title, 'content': page_content})
        
    if request.method == 'POST':
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content').replace('\r', '')

            if content == page_content:
                messages.error(request, f"No changes have been made.")
                return redirect(f'/wiki/{title}/edit-entry')
            
            messages.success(request, f"{title} entry has been editted.")
            util.save_entry(title, content)

            return redirect('/wiki/' + title)

    return render(request, 'encyclopedia/edit_entry.html', {
        'title': title,
        'form': form
    })