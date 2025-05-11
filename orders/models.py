# orders/models.py

from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.cart.items.all())
