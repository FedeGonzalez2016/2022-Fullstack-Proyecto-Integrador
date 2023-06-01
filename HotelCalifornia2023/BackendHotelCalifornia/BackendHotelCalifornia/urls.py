
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from login.views import LoginView
from register.views import SingupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'), # OK 
    path('singup/', SingupView.as_view(), name='singup'), 
]
