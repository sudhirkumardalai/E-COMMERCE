from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField

class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    phone_field = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return self.user.username

class catagory(models.Model):
    catagory_name = models.CharField(max_length=200)

    def __str__(self):
        return self.catagory_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    catagory = models.ForeignKey('catagory', on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.FloatField(default=0.0)
    product_available_count = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={
            "pk": self.pk
        })

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_final_price(self):
        return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, unique=True, default=None, blank=True, null=True)
    datetime_of_payment = models.DateTimeField(auto_now_add=True)  # Correct field name
    order_delivered = models.BooleanField(default=False)
    order_received = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    # def get_total_price(self):
    #     total = sum(order_item.get_total_item_price() for order_item in self.items.all())
    #     return total

    def get_total_count(self):
        return self.items.count()
class CheckoutAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=200)
    country = CountryField(multiple=False)  
    zip_code = models.CharField(max_length=20) 

    def __str__(self):
        return self.user.username   
