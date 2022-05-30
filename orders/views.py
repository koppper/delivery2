from django.contrib import messages
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        message_name = request.POST['first_name']
        message_email = request.POST['email']
        message = request.POST['address']
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                send_mail(message_name, message, message_email,
                                 ['komaliyeva@gmail.com'], fail_silently=False)
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
    return render(request, 'orders/order/create.html', {'cart': cart})

