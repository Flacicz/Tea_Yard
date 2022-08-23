from decimal import Decimal
from django.conf import settings
from TeaYardApp.models import Products


class Cart(object):

    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Перебираем товары в корзине и получаем товары из базы данных"""
        product_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        product = Products.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in product:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            # convert to string first (to be able call isnumeric method)
            price = str(item['price'])
            # check if price string is numeric
            if price.isnumeric():
                price = Decimal(price)
            else:
                # handle bad value (raise error or whatever depending on your logic)
                raise ValueError('price must be numeric value')
            item['total_price'] = price * item['quantity']
            yield item

    def __len__(self):
        """Считаем сколько товаров в корзине"""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """Добавляем товар в корзину или обновляем его количество."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, product):
        """Удаляем товар"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self, price):
        # получаем общую стоимость
        return sum(Decimal(price) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()


