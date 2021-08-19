from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from django.views.generic import TemplateView, FormView

from .forms import ContactForm


class IndexView(FormView):
    form_class = ContactForm
     
    template_name = "index.html"
 
    success_url ="index"

    def form_valid(self, form):
        name=form.cleaned_data.get('name')
        email=form.cleaned_data.get('email')
        body = form.cleaned_data.get('body')
        subject = form.cleaned_data.get('subject')
        message = f' {name} => {body}'
        send_mail(subject, 
            message,email , [settings.EMAIL_HOST_USER], fail_silently = False)
        return redirect('index') 