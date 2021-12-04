from django.urls import path

from . import views

urlpatterns = [
    path('', views.firstpage, name= 'firstpage'),
    path('terms', views.terms, name= 'terms'),
    path('price', views.price, name='price'),
    path('registration', views.registration, name= 'registration'),
    # path('main_input', views.main_input, name= 'main_input'),
    # path('home', views.home, name= 'home'),
    # path('body_output',views.body_output, name= 'body_output'),
    # path('exercise' ,views.exercise, name = 'exercise'),
    # path('burn_output' ,views.burn_output, name = 'burn_output'),
    # path('food' , views.food, name='food'),
    # path('food_output' , views.food_output, name='food_output'),
    # path('disease', views.disease, name='disease'),
    # path('yoga' , views.yoga, name='yoga'),
    # path('kriya' , views.kriya, name='kriya'),
    # path('yog_nidra' , views.yog_nidra, name='yog_nidra'),
    # path('system_wise' , views.system_wise, name='system_wise'),
    # path('upnishdic' , views.upnishdic, name='upnishdic'),
    # path('natal' , views.natal, name='natal'),
    # path('more' , views.more, name='more'),
]