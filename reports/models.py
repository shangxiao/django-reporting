from django.db import models


class Location(models.Model):
    name = models.CharField()


class Store(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    address = models.CharField()


class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    sale = models.IntegerField()
