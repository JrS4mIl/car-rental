from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'cars': paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_search':body_search,

    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    context = {
        'single_car': single_car
    }
    return render(request, 'cars/car-details.html', context)


def search(request):
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model=request.GET['model']
        if 'model':
            cars=cars.filter(model__icontains=model)

    if 'city' in request.GET:
        city=request.GET['city']
        if 'city':
            cars=cars.filter(city__icontains=city)

    if 'year' in request.GET:
        year=request.GET['year']
        if 'year':
            cars=cars.filter(year__icontains=year)
    if 'body' in request.GET:
        body=request.GET['body']
        if 'body':
            cars=cars.filter(body_style__icontains=body)

    if 'transmission' in request.GET:
        transmission=request.GET['transmission']
        if 'transmission':
            cars=cars.filter(transmission__icontains=transmission)

    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)


    context = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,
        'transmission_search':transmission_search,
    }
    return render(request, 'cars/search.html', context)
