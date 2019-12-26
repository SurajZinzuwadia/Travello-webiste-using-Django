from django.urls import path
from . import views
urlpatterns = [
    path("register",views.register,name='register'),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("mumbai",views.destination.mumbai,name="mumbai"),
    path("hydrabad",views.destination.hydrabad,name="hydrabad"),
    path("bengaluru",views.destination.bengaluru,name="bengaluru"),
    path("pune",views.destination.pune,name="pune"),
    path("surat",views.destination.surat,name="surat"),
    
]