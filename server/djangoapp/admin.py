from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.
# CarModelInline class
class CarModelAdmin(admin.ModelAdmin):
    fields = [
        'car_make',
        'name',
        'type',
        'year'
    ]
# CarModelAdmin class
admin.site.register(CarModel, CarModelAdmin)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description'
    ]
# Register models here
admin.site.register(CarMake, CarMakeAdmin)