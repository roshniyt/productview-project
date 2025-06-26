from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from authenticate.models import HeroSection, SampleResult  # adjust model names

@login_required(login_url='login') # Ensure user is logged in to access the dashboard
def dashboard_view(request):
    hero = HeroSection.objects.all()
    result = SampleResult.objects.all()
    return render(request, 'dashboard/home.html', {'hero': hero, 'result': result})

def logout_view(request):
    logout(request)
    return redirect('login')

def about_view(request):
    return render(request, 'dashboard/about.html')

def contact_view(request):
    return render(request, 'dashboard/contact.html')

def service_view(request):
    return render(request, 'dashboard/service.html')

