from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from django.urls import reverse


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['cost'],
                                         quantity=item['quantity'])
            cart.clear()

            order_created.delay(order.id)
            request.session['order.id'] = order.id
            return redirect(reverse('payment:process'))  # or paygateway
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})
