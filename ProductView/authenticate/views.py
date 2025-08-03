from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import HeroSection 
from .models import SampleResult

def register_view(request):
    if request.method == 'POST':
        # print(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        # print(email, username, password1, password2)
       
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'authenticate/register.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'authenticate/register.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Registration successful")
        return redirect('login')

    return render(request, 'authenticate/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1= request.POST.get('password1')  
        user = authenticate(request, username=username, password=password1)
        
        if user is not None:
                  login(request, user)
                  return redirect('dashboard')
        else:
             messages.error(request, "Invalid username or password")


    return render(request,'authenticate/login.html')



def index(request):
    hero = HeroSection.objects.all()
    result = SampleResult.objects.all() 
    params = {
        'hero': hero,
        'result': result,
    }
    return render(request, 'authenticate/index.html',params)