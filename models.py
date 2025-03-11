from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    purchases = models.TextField()
    feedback = models.TextField()

    def __str__(self):
        return self.name

