from django import forms

INITIAL_CONTENT = ("## Sample Markdown Heading\n"
                    "**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")

class EntryForm(forms.Form):
    title = forms.CharField(initial='Title', label='Title', max_length=25)
    content = forms.CharField(initial= INITIAL_CONTENT, widget=forms.Textarea)

class EditEntryForm(forms.Form):
    title = forms.CharField(initial='Title', disabled=True, label='Title', max_length=25)
    content = forms.CharField(initial= INITIAL_CONTENT, widget=forms.Textarea)