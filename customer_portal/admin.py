from django.contrib import admin

from .models import Customer, Orders
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display= ('mobile', 'city_Pincode', 'user')
    @admin.display(empty_value='unknown')

    def city_Pincode(self, obj):
        return (obj.area.city, obj.area.pincode)

class OrderAdmin(admin.ModelAdmin):
    list_display= ('user', 'car_dealer', 'rent', 'vehicle', 'days', 'is_complete')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Orders, OrderAdmin)