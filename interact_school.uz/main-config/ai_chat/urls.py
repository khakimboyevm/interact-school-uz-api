from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('chatai/', views.chat_view, name='chat_ai'),
]
