import os

import stripe
from dotenv import load_dotenv

load_dotenv()


class Stripe_API:

    def __init__(self):
        self.stripe = stripe
        self.stripe.api_key = os.getenv('STRIPE_API_KEY')

    def get_products(self):
        '''Получение всех банковских продуктов Stripe'''
        return self.stripe.Product.list()

    def create_product(self, name, price):
        '''Создание банковского продукта Stripe'''
        product = self.stripe.Product.create(name=name)
        return self.stripe.Price.create(
            currency='rub',
            unit_amount=price * 100,
            product=product.id,
        )

    def create_session(self, price_id):
        '''Создание сессии Stripe'''
        return self.stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": price_id, "quantity": 1}],
            mode="payment",
        )

    def retrieve_session(self, id):
        '''Востановление сессии Stripe'''
        return stripe.checkout.Session.retrieve(
            id
        )
