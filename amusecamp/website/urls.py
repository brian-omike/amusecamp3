from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('amuse_camp.html', views.amuse_camp, name="amuse_camp"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('pricing.html', views.pricing, name="pricing"),
    path('activities.html', views.activities, name="activities"),
]
