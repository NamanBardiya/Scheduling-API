from django.urls import path

from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('check',views.check,name='check'),
    path('ping',views.servercheck,name='ping'),
]