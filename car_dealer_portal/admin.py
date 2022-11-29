from django.contrib import admin

# Register your models here.
from .models import Area, CarDealer, Vehicles

class AreaAdmin(admin.ModelAdmin):
    list_display = ['pincode', 'city']

class CarDealerAdmin(admin.ModelAdmin):
    list_display = ('car_dealer', 'mobile', 'city_pincode', 'wallet')

    @admin.display(empty_value='unknown')
    def city_pincode(self, obj):
        return (obj.area.city, obj.area.pincode)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'color','dealer', 'city_pincode', 'capacity', 'is_available', 'description', 'img']

    @admin.display(empty_value='unknown')
    def city_pincode(self, obj):
        return (obj.area.city, obj.area.pincode)


admin.site.register(Area, AreaAdmin)
admin.site.register(CarDealer, CarDealerAdmin)
admin.site.register(Vehicles, VehicleAdmin)