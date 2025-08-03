from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from authenticate.models import HeroSection, SampleResult  
from .models import Product

@login_required(login_url='login') # To Ensure user is logged in to access the dashboard
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

def scan_view(request):
    context = {}

    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        product = Product.objects.filter(barcode=barcode).first()

        if product:
            
            try:
                calories = float(product.calories)
                sugar = float(product.sugar)
                fat = float(product.fat)
            except ValueError:
                context['error'] = "Nutrition values couldn't be processed."
                return render(request, 'dashboard/scan.html', context)

          
            if calories < 200 and sugar < 10 and fat < 5:
                is_healthy = True
                reason = "Low in calories, sugar, and fat —  Healthy To Consume."
            else:
                is_healthy = False
                reason = "High calories, sugar, or fat — Not Healthy."

            
            context['product'] = product
            context['is_healthy'] = is_healthy
            context['reason'] = reason
        else:
            context['error'] = "No product found with this barcode."

    return render(request, 'dashboard/scan.html', context)