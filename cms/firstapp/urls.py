from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('consultancy',views.consultancy),
    path('services',views.services),
    path('portfolio',views.portfolio),
    path('contact',views.contact),
    path('about',views.about),
    path('admin',views.admin),
    path('adminhome',views.adminhome),
    path('cardTask',views.cardTask),
    path('card',views.card),
    path('cardTaskdone',views.cardTaskdone),
    path('contactTask',views.contactTask),
    path('consultancyTask',views.consultancyTask),
    path('logout',views.logout),
    path('adminhomeedit',views.adminhomeedit),
    path('cardTaskwork',views.cardTaskwork),
    path('cardTaskbenifits',views.cardTaskbenifits),


]