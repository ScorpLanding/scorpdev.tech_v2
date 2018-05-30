from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='Projects'),
    path('insta', views.instloader, name='InstaLoad')
]