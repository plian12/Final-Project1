from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# The `Customer` class defines a model with fields for user, name, email, and points.
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user
# The `MenuItem` class defines attributes for a menu item including name, description, and price.

class MenuItem(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

# The Order class represents an order made by a customer, containing multiple items and the date of
# the order.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.user.username}"
    
# The `Points` class represents a model with fields for customer, points, and order in a Django
# application.
class Points(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='points_instances')
    points = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.user.username} has {self.points} points"