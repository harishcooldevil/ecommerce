from django.contrib import admin
from .models import Item, Order, OrderItem, BillingAddress, Profile, Portfolio


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(BillingAddress)
admin.site.register(Profile)
admin.site.register(Portfolio)
