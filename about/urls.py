"""
Urls for About Pages and Contact Form
"""

from django.urls import path
from . import views
from .views import contact_view, success_view


urlpatterns = [
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', contact_view, name='contact_us'),
    path('success/', success_view, name='success'),
]
