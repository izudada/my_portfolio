from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'class':'contact__input' }))
    subject = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Subject', 'class':'contact__input' }))
    email = forms.EmailField(widget=forms.EmailInput( attrs={'placeholder':'Email', 'class':'contact__input'}))
    
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'contact__input'}))