from django.contrib import admin
from . import models
# Register your models here.
from .models import Blog
from .models import Customer
admin.site.register(Customer)


class EventAdminArea(admin.AdminSite):
    site_header = 'Event Organizer Area'

eventorganizing_site = EventAdminArea(name='EventAdmin')
eventorganizing_site.register(models.Event)


admin.site.register(Blog)