from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    rating = models.IntegerField()
    cuisine = models.CharField(max_length=50)


class RestaurantMenu(models.Model):
    day = models.DateField()
    dish_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()

class VotingResult(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(RestaurantMenu, on_delete=models.CASCADE)
    vote = models.BooleanField(default=False)