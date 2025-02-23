
from django.contrib import admin
from django.urls import path
from event.views import home
from event.views import RegisterPage
from event.views import Login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', RegisterPage, name="register"),
    path('login/', Login, name="login"),


]
