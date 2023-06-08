
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import LoginView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth_login'),
]