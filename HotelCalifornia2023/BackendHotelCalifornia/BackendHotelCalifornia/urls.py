
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from login.views import LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'), # OK 
]
