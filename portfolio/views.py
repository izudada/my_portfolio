from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from django.views.generic import TemplateView, FormView


class IndexView(TemplateView):
    template_name = 'index.html'


def contact_me(request):
    if request.method == 'POST':
        recepient = request.POST['email']
        name = request.POST['name']
        body = request.POST['message']
        subject = 'Portfolio Contact'
        message = f'{name} => {body}'
        send_mail(subject, 
            message,recepient , [settings.EMAIL_HOST_USER], fail_silently = False)
        messages.info(request, "Info: Thanks, I have gladly received your mail and enroute to read with anticipation.")
        return redirect('index')