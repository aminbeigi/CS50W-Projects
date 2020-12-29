from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(initial='Title', label='Title', max_length=25)
    content = forms.CharField(initial= ("## Sample Markdown Heading\n"
                                        "**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
                                        widget=forms.Textarea)