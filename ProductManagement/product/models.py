from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(unique = True, primary_key=True)
    name = models.CharField(null = False)
    sku = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     customer_name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_created=True) #auto_nowadd

#     def __str__(self):
#         return self.customer_name

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item') #order can access orderitems using keyword 'item' eg obj.item
#     items = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default= 1)
#     # tag = models.ManyToManyField(Category)

#     def __str__(self):
#         return f"{self.items.name} (x{self.quantity})"
    
# class Category(models.Model):
#     CATEGORY = ['stationary', 'apparels', 'office use', 'furniture', 'games', 'skincare', 'beauty products', 'accessories' , 'kitchen essentials']
#     category = models.CharField(choices= CATEGORY)

#     def __str__(self):
#         return self.category



class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True) #auto_nowadd

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_vars_json()

    def update(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_vars_json()

    def update_vars_json(self):
        order_items = OrderItem.objects.filter(order=self)
        vars_json = {var.items: var.quantity for var in order_items}
        self.vars_json = vars_json
        super().save()
        
    def __str__(self):
        return self.customer_name
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item') #order can access orderitems using keyword 'item' eg obj.item
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default= 1)
    # tag = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.items.name} (x{self.quantity})"