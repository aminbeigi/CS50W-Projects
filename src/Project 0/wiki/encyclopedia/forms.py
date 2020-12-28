from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=25)
    content = forms.CharField(widget=forms.Textarea)
