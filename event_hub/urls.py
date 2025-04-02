
# from django.contrib import admin
# from django.urls import path
# from event.views import home
# # from event.views import RegisterPage
# from event.views import LoginPage
# from event.views import LogoutPage
# from event.views import signupPage,about_us, blogs,create_event, edit_event, create_blog, edit_blog,create_voting_event, edit_voting_event
# from event.admin import eventorganizing_site
# # from event.admin import event_site





# urlpatterns =[
#     path('admin/', admin.site.urls),
#     path('', home, name="home"),
#     # path('register/', RegisterPage, name="register"),
#     path('login/', LoginPage, name="login"),
#     path('logout/', LogoutPage, name="logout" ),
#     path('signup/', signupPage, name="signup"),
#     path('about/', about_us, name="about_us"),
#     path('blog/', blogs, name="blog"),
#     # path('event_admin/', event_site.urls, name="event_admin"),
#     path('eventadmin/', eventorganizing_site.urls, name="eventadmin"),
    


# ]

# admin.site.index_title="Pokhara Event Hub"
# admin.site.site_header="Pokahara Event Hub Adminsite"
# admin.site.site_title="Eventhub"






# urlpatterns = [
#     path('eventadmin/events/create/', create_event, name="create_event"),
#     path('eventadmin/events/edit/<int:event_id>/', edit_event, name="edit_event"),
    
#     path('eventadmin/blogs/create/', create_blog, name="create_blog"),
#     path('eventadmin/blogs/edit/<int:blog_id>/', edit_blog, name="edit_blog"),
    
#     path('eventadmin/voting_events/create/', create_voting_event, name="create_voting_event"),
#     path('eventadmin/voting_events/edit/<int:voting_event_id>/', edit_voting_event, name="edit_voting_event"),
# ]


from django.contrib import admin
from django.urls import path
from event.views import home, LoginPage, LogoutPage, signupPage, about_us, blogs, create_event, edit_event, create_blog, edit_blog, create_voting_event, edit_voting_event, blog_detail
from event.admin import eventorganizing_site
from event.views import events_page
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    # Admin and Event Manager paths
    path('admin/', admin.site.urls),
    path('eventadmin/', eventorganizing_site.urls, name="eventadmin"),
    
    # Home and user-related paths
    path('', home, name="home"),
    path('login/', LoginPage, name="login"),
    path('logout/', LogoutPage, name="logout"),
    path('signup/', signupPage, name="signup"),
    path('about/', about_us, name="about_us"),
    path('blog/', blogs, name="blog"),
    # path('blog_detail/', blog_detail, name="blog"),


    # Event and Blog Management paths
    path('eventadmin/events/create/', create_event, name="create_event"),
    path('eventadmin/events/edit/<int:event_id>/', edit_event, name="edit_event"),
    path('eventadmin/blogs/create/', create_blog, name="create_blog"),
    path('eventadmin/blogs/edit/<int:blog_id>/', edit_blog, name="edit_blog"),
    path('eventadmin/voting_events/create/', create_voting_event, name="create_voting_event"),
    path('eventadmin/voting_events/edit/<int:voting_event_id>/', edit_voting_event, name="edit_voting_event"),
    path('events/', events_page, name='events_page'),
    path('blog/<str:title>/', blog_detail, name="blog_detail"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)