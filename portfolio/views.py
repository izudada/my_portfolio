from django.http import request
from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.views.generic import FormView

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
        messages.add_message(
            message=_('Thanks, your message was well received. Will reply asap'),
            request=self.request,
            level=messages.SUCCESS
        )
        return redirect('index') 