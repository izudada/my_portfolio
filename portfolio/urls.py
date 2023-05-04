from django.urls import  include, path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('', include('django.contrib.auth.urls')),
    path('portfolio/', views.portfolio, name="portfolio"),
]