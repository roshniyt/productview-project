from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'), 
    path('logout/',views.logout_view,name='logout'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('service/', views.service_view, name='service'),
    path('scan/', views.scan_view, name='scan'),
   
]