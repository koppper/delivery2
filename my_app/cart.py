from decimal import Decimal
from django.conf import settings
from models import Products
class Cart(object):
    def __init__(self, request):
        """Инициализация объекта корзины."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
        cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
