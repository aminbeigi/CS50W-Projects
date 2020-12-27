from django import forms

class SearchForm(forms.Form):
    search_form = forms.CharField(label='Search Form', max_length=100)