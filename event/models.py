from django.db import models



# Create your models here.
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50,default='hemantagurung12@gmail.com')
    

    #String representation of the model 
    def __str__(self):
        return self.user.username
    
    class meta:
        db_table = 'event_users'



class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', default='default.jpg')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
