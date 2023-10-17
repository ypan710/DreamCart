from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartAdmn(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemAdmn(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    
admin.site.register(Cart, CartAdmn)
admin.site.register(CartItem, CartItemAdmn)

