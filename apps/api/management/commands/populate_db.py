# Imports the random module to generate random samples
import random
# Imports the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Imports the base class for creating custom management commands in Django
from django.core.management.base import BaseCommand
# Imports a utility to generate random text
from django.utils import lorem_ipsum
#Imports the models User, Product, Order and OrderItem from the specified Django apps
from apps.api.models import User, Product, Order, OrderItem

#Define a new management command by subclassing BaseCommand
class Command(BaseCommand):
    # Provides a brief description of what the command does.
    help = 'Creates application data'
    # This method is called when the command is executed
    def handle(self, *args, **kwargs):
        # It checks if a user with the username 'admin' already exists using
        user = User.objects.filter(username='admin').first()
        # If the user does not exist, it creates a new superuser with the username and password
        if not user:
            user = User.objects.create_superuser(username='admin', password='test')

        # create products - name, desc, price, stock, image
        products = [
            Product(name="A Scanner Darkly", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4),
            Product(name="Coffee Machine", description=lorem_ipsum.paragraph(), price=Decimal('70.99'), stock=6),
            Product(name="Velvet Underground & Nico", description=lorem_ipsum.paragraph(), price=Decimal('15.99'), stock=11),
            Product(name="Enter the Wu-Tang (36 Chambers)", description=lorem_ipsum.paragraph(), price=Decimal('17.99'), stock=2),
            Product(name="Digital Camera", description=lorem_ipsum.paragraph(), price=Decimal('350.99'), stock=4),
            Product(name="Watch", description=lorem_ipsum.paragraph(), price=Decimal('500.05'), stock=0),
        ]

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()


        # create some dummy orders tied to the superuser
        for _ in range(3):
            # create an Order with 2 order items
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1,3)
                )