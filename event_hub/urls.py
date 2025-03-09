
from django.contrib import admin
from django.urls import path
from event.views import home
# from event.views import RegisterPage
from event.views import LoginPage
from event.views import LogoutPage
from event.views import signupPage,about_us, blogs






urlpatterns =[
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    # path('register/', RegisterPage, name="register"),
    path('login/', LoginPage, name="login"),
    path('logout/', LogoutPage, name="logout" ),
    path('signup/', signupPage, name="signup"),
    path('about/', about_us, name="about_us"),
    path('blog/', blogs, name="blog"),
]