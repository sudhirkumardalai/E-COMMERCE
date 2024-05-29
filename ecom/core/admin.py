from django.contrib import admin
from core.models import *
admin.site.register(Customer)
admin.site.register(catagory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CheckoutAddress)