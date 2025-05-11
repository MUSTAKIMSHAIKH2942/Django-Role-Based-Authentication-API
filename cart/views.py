# cart/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from products.models import Product
from orders.models import Order

@login_required
def add_to_cart(request, product_id):
    """Add product to cart."""
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Add item to cart or update quantity if it exists
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    """Display the user's cart."""
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart/view_cart.html', {'cart': cart})

@login_required
def checkout(request):
    """Checkout the user's cart and create an order."""
    cart = Cart.objects.filter(user=request.user).first()
    order = Order.objects.create(user=request.user, cart=cart)
    cart.delete()  # Clear the cart after placing the order

    return redirect('orders:order_confirmation', order_id=order.id)

