import factory

from reports.models import Location, Sale, Store


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store


class SaleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sale
