from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail

from django.views.generic import TemplateView, FormView


class IndexView(TemplateView):
    template_name = 'index.html'


def subscribe(request):
    if request.method == 'POST':
        sub = request.POST
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'index.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})