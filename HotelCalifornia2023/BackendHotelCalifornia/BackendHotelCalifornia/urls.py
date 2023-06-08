
from django.contrib import admin
from django.urls import path, include
from register.views import SingupView
from logout.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hotel_auth.urls')), # OK 
    path('singup/', SingupView.as_view(), name='singup'), 
    path('logout/', LogoutView.as_view(), name='logout'),
]
