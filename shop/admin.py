from django.contrib import admin
from .models import Role, Category, Product, Wishlist, Offer, Cart,  Order, OrderDetail, Checkout, Review

admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Offer)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Checkout)
admin.site.register(Review)