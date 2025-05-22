
from django.contrib import admin
from .models import Product, Order, OrderItem


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sku', 'price', )  # Optional: customize admin list view
    # search_fields = ('id', )
# Register your models here.

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer_name','created_at', 'items_list',)
#     def items_list(self, obj):
#         item_string = []
#         for i in obj.item.all():
#             item_string.append(str(i))
#         return ",".join(item_string)
    
# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order', 'items', 'quantity',)

# @admin.register(OrderItem)
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    can_delete = True

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ["var_name", "var_desc"]
    #     return []
    
    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0 
        return super().get_extra(request, obj, **kwargs)
    
    # def has_add_permission(self, request, obj):
    #     if obj: 
    #         return True
    #     return True  

# @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ('vars_json',)
    inlines = [OrderItemAdmin]
    list_display = ('customer_name','created_at', 'items_list',)
    def items_list(self, obj):
        item_string = []
        for i in obj.item.all():
            item_string.append(str(i))
        return ",".join(item_string)

    # def Status(self, obj):
    #     color = 'green' if obj.status == 'Active' else 'red'
    #     return format_html('<span style="color: {};">{}</span>', color, obj.status)
    
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ["email_code"]
    #     return []


class OrderItemStandaloneAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'items', 'quantity')


# admin.site.register(OrderItem, Order, Product)
admin.site.register(Product, ProductAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemStandaloneAdmin)

'''
Username = 'hb'
Email address: admin@admin.com
Password: hbdev
'''