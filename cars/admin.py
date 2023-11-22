from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40' style='border-radius:30px'/>".format(object.car_photo.url))

    thumbnail.short_description = 'car image'
    list_display = ('id','thumbnail','car_title', 'color', 'city', 'model', 'year', 'body_style', 'is_featured')
    list_display_links = ('id','thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title','model','fuel_type','color')
    list_filter = ('city','fuel_type')
admin.site.register(Car,CarAdmin)
