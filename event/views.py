from django.shortcuts import render,redirect
# from django.contrib.auth.models import user
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# from django.contrib.auth.models import signup
from .models import Customer

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html") 
    else:
        return redirect( "/login")

# def RegisterPage(request):
#     return render(request, "event/register.html") 

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/login')    

        else:
            return render(request, "login.html")


def signupPage(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
          
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            customer = Customer.objects.create(user=user, username=username, email=email, phonenumber=phonenumber)
            customer.save()

           
            login(request, user)
            return redirect('/')
        else:
            return redirect('/signup')
    else:
        return render(request, "signup.html") 
    
def LogoutPage(request):
    logout(request)
    return redirect('/login')



from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Customer, Event  # Assuming you have an Event model

def home(request):
    # Fetch upcoming events (you may filter based on your database)
    events = Event.objects.filter(is_active=True).order_by('date')[:5]  # Show only 5 upcoming events

    context = {
        'events': events
    }
    
    return render(request, "home.html") 


from django.shortcuts import render
from .models import Event  # Assuming Event model exists

def about_us(request):
    # Fetch some past events to showcase (adjust filtering based on your logic)
    past_events = Event.objects.filter(is_active=True).order_by('-date')[:3]  # Show latest 3 past events

    context = {
        'past_events': past_events
    }
    
    return render(request, "about.html")


from django.shortcuts import render
from .models import Blog  # Assuming you have a Blog model

from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogs(request):
    latest_blog = Blog.objects.filter(is_published=True).order_by('-date_posted').first()
    more_blogs = Blog.objects.filter(is_published=True).order_by('-date_posted')[1:5]  # Exclude the latest one

    context = {
        'latest_blog': latest_blog,
        'more_blogs': more_blogs,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

