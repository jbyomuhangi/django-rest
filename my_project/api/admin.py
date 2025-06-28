from django.contrib import admin

# Register your models here.
from .models import User, Product, Order, OrderItem


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
