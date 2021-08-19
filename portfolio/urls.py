from django.urls import  include, path
from . import views


urlpatterns = [
    path('contact_me/', views.contact_me, name="contact_me"),
    path('', views.IndexView.as_view(), name="index"),
    path('', include('django.contrib.auth.urls')),
]