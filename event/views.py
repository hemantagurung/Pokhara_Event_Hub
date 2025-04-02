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

# from django.shortcuts import render, get_object_or_404
# from .models import Blog

# def blogs(request):
#     latest_blog = Blog.objects.filter(is_published=True).order_by('-date_posted').first()
#     more_blogs = Blog.objects.filter(is_published=True).order_by('-date_posted')[1:5]  # Exclude the latest one
#     context = {
#         'latest_blog': latest_blog,
#         'more_blogs': more_blogs,
#     }
    
#     return render(request, 'blog.html', context)



# def blog_detail(request):
#     # blog = get_object_or_404(Blog, id=blog_id)

#     lastest_blog = Blog.objects.all()
#     return render(request, 'blog.html', {'blog' :  lastest_blog})
#     # return render(request, 'event.html', {'events': events})


from django.shortcuts import render, get_object_or_404
from event.models import Blog

def blogs(request):
    latest_blog = Blog.objects.filter(is_published=True).order_by('-date_posted').first()
    more_blogs = Blog.objects.filter(is_published=True).order_by('-date_posted')[1:5]
    print("Latest Blog Title:", latest_blog.title if latest_blog else "None")
    print("More Blogs Titles:", [blog.title for blog in more_blogs])
    context = {
        'latest_blog': latest_blog,
        'more_blogs': more_blogs,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, title):
    print("Requested Title:", title)  # Debug
    blog = get_object_or_404(Blog, title=title, is_published=True)
    return render(request, 'blog_detail.html', {'blog': blog})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Blog, VotingEvent


def create_event(request):
    if request.method == "POST":
        form = Event(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventadmin')
    else:
        form = Event()
    return render(request, 'create_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = Event(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventadmin')
    else:
        form = Event(instance=event)
    return render(request, 'edit_event.html', {'form': form})


def create_blog(request):
    if request.method == "POST":
        form = Blog(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = Blog()
    return render(request, 'create_blog.html', {'form': form})

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = Blog(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = Blog(instance=blog)
    return render(request, 'edit_blog.html', {'form': form})



def create_voting_event(request):
    if request.method == "POST":
        form = VotingEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voting_event_list')
    else:
        form = VotingEvent()
    return render(request, 'create_voting_event.html', {'form': form})

def edit_voting_event(request, voting_event_id):
    voting_event = get_object_or_404(VotingEvent, id=voting_event_id)
    if request.method == "POST":
        form = VotingEvent(request.POST, instance=voting_event)
        if form.is_valid():
            form.save()
            return redirect('voting_event_list')
    else:
        form = VotingEvent(instance=voting_event)
    return render(request, 'edit_voting_event.html', {'form': form})

from django.shortcuts import render
from .models import Event

def events_page(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
