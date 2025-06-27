from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from authenticate.models import HeroSection, SampleResult  # adjust model names
from .models import Product

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

def scan_view(request):
    if 'scanned_products' not in request.session:
        request.session['scanned_products'] = []

    context = {}

    if request.method == 'POST':
        barcode_input = request.POST.get('barcode')
        product = Product.objects.filter(barcode=barcode_input).first()

        if product:
            calories = str(product.calories).lower().replace('kcal', '').replace('cal', '').strip()
            sugar = str(product.sugar).lower().replace('g', '').strip()
            fat = str(product.fat).lower().replace('g', '').strip()

            try:
                calories = float(calories)
                sugar = float(sugar)
                fat = float(fat)

                if calories < 200 and sugar < 10 and fat < 5:
                    is_healthy = True
                    reason = "This product is considered healthy because it has low calories, sugar, and fat."
                else:
                    is_healthy = False
                    reason = "This product is not healthy because it has high calories, sugar, or fat."

                
                scanned_product = {
                    'name': product.name,
                    'image': product.image.url,
                    'calories': product.calories,
                    'sugar': product.sugar,
                    'fat': product.fat,
                    'category': product.category,
                    'is_healthy': is_healthy,
                    'reason': reason
                }

                scanned_products = request.session['scanned_products']
                scanned_products.append(scanned_product)
                request.session['scanned_products'] = scanned_products

            except ValueError:
                context['error'] = "Nutrition values couldn't be processed."
        else:
            context['error'] = "No product found with this barcode."

    if request.GET.get('clear') == '1':
        request.session['scanned_products'] = []

    context['scanned_products'] = request.session.get('scanned_products', [])
    return render(request, 'dashboard/scan.html', context)
