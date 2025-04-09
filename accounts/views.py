from django.shortcuts import render,redirect 
from django.contrib import auth
from django.contrib.auth.models import User
from Mydiary.views import show

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def login(request):
    if request.method == "POST":
        # check if a user exists
        # with the username and password
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(show)
        else:
            return render(request, 'home.html', {'error': "Invalid Login credentials."})
    else:
        return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        # to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            # both the passwords matched
            # check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username= request.POST['username'],password= request.POST['password'])
              
                auth.login(request, user)
                return redirect(home)
        else:
            return render(request, 'register.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect(home)
