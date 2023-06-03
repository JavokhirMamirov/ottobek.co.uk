from django.urls import path
from home.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('send-message', send_message_view, name='send_message')
]