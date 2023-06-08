
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import LoginView, LogoutView, SingupView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/singup/', SingupView.as_view(), name='auth_singup'),
]