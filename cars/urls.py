
from django.urls import path
from .views import cars,car_detail
urlpatterns = [
    path('',cars,name='cars'),
    path('/<int:id>',car_detail,name='car_detail')


]
