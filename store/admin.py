from django.contrib import admin
from store.models.customer import Customer
from store.models.category import Category
from store.models.orders import Order
from store.models.product import Products




admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Products)





# Register your models here.
