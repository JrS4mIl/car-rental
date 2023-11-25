from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages



# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
                          state=state, email=email, phone=phone, message=message)
        #admin_info=User.objects.get(is_superuser=True)
        #admin_email=admin_info.email
        #send_mail(
        #    'New Car Inquiry',
        #    'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.',
        #    'ysamil072@gmail.com',
        #    [admin_email],
        #    fail_silently=False,
        #)
        contact.save()
        messages.success(request, 'Thank requests has been submited,we will get back to your shortly.')
        return redirect('/cars/'+car_id)
