# Import the models module from Django to define database models
from django.db import models

# Define a new model class called Product that inherits from models.Model
class Product(models.Model):
    # Define a character field for the product name with a maximum length of 200 characters
    name = models.CharField(max_length=200)
    # Define a text field for a detailed product description
    description = models.TextField()
    # Define a decimal field for the product price with up to 10 digits total and 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Define a positive integer field for the quantity of the product in stock
    stock = models.PositiveIntegerField()
    # Define an image field for uploading a product image to the 'products/' directory, allowing it to be blank or null
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Decorator to define a property method
    @property
    # Define a method to check if the product is in stock
    def in_stock(self):
        #Return True if stock is greater than 0, otherwise return False
        return self.stock > 0
    
     # Define a string representation method for the Product model
    def __str__(self):
        # Return the name of the product as its string representation
        return self.name


