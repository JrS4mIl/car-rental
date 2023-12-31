from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,

    }
    return render(request, 'pages/index.html', context)


def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method=='POST':
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            phone = request.POST['phone']
            message = request.POST['message']
            messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
            return redirect('contact')
    return render(request, 'pages/contact.html')

