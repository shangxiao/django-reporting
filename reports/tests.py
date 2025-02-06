from datetime import datetime, timezone

import factory
import pytest

from reports.models import Sale, Location, Store
from reports.services import (
    series_1_to_10,
    series_date_range_jan_2025,
    series_even_numbers_to_20,
)

pytestmark = pytest.mark.django_db


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store


class SaleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sale


def test_series_1_to_10():
    assert series_1_to_10() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_series_even_numbers_to_20():
    assert series_even_numbers_to_20() == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def test_series_date_range_jan_2025():
    assert series_date_range_jan_2025() == [
        datetime(2025, 1, 1, tzinfo=timezone.utc),
        datetime(2025, 1, 2, tzinfo=timezone.utc),
        datetime(2025, 1, 3, tzinfo=timezone.utc),
        datetime(2025, 1, 4, tzinfo=timezone.utc),
        datetime(2025, 1, 5, tzinfo=timezone.utc),
        datetime(2025, 1, 6, tzinfo=timezone.utc),
        datetime(2025, 1, 7, tzinfo=timezone.utc),
        datetime(2025, 1, 8, tzinfo=timezone.utc),
        datetime(2025, 1, 9, tzinfo=timezone.utc),
        datetime(2025, 1, 10, tzinfo=timezone.utc),
        datetime(2025, 1, 11, tzinfo=timezone.utc),
        datetime(2025, 1, 12, tzinfo=timezone.utc),
        datetime(2025, 1, 13, tzinfo=timezone.utc),
        datetime(2025, 1, 14, tzinfo=timezone.utc),
        datetime(2025, 1, 15, tzinfo=timezone.utc),
        datetime(2025, 1, 16, tzinfo=timezone.utc),
        datetime(2025, 1, 17, tzinfo=timezone.utc),
        datetime(2025, 1, 18, tzinfo=timezone.utc),
        datetime(2025, 1, 19, tzinfo=timezone.utc),
        datetime(2025, 1, 20, tzinfo=timezone.utc),
        datetime(2025, 1, 21, tzinfo=timezone.utc),
        datetime(2025, 1, 22, tzinfo=timezone.utc),
        datetime(2025, 1, 23, tzinfo=timezone.utc),
        datetime(2025, 1, 24, tzinfo=timezone.utc),
        datetime(2025, 1, 25, tzinfo=timezone.utc),
        datetime(2025, 1, 26, tzinfo=timezone.utc),
        datetime(2025, 1, 27, tzinfo=timezone.utc),
        datetime(2025, 1, 28, tzinfo=timezone.utc),
        datetime(2025, 1, 29, tzinfo=timezone.utc),
        datetime(2025, 1, 30, tzinfo=timezone.utc),
        datetime(2025, 1, 31, tzinfo=timezone.utc),
    ]


@pytest.fixture
def setup_sales():
    melb = LocationFactory(name="Melbourne")
    bourke = StoreFactory(address="Bourke St", location=melb)

    SaleFactory(store=bourke, timestamp="2025-01-01T08:30:00Z", sale=150)
    SaleFactory(store=bourke, timestamp="2025-01-01T12:15:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-01T15:45:00Z", sale=120)
    SaleFactory(store=bourke, timestamp="2025-01-02T10:00:00Z", sale=175)
    SaleFactory(store=bourke, timestamp="2025-01-02T14:00:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-02T18:30:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-03T09:00:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-03T13:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-03T16:00:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-04T11:15:00Z", sale=160)
    SaleFactory(store=bourke, timestamp="2025-01-04T15:00:00Z", sale=140)
    SaleFactory(store=bourke, timestamp="2025-01-04T19:00:00Z", sale=250)
    SaleFactory(store=bourke, timestamp="2025-01-05T08:45:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-05T12:30:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-05T17:00:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-06T10:15:00Z", sale=170)
    SaleFactory(store=bourke, timestamp="2025-01-06T13:00:00Z", sale=185)
    SaleFactory(store=bourke, timestamp="2025-01-06T16:30:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-07T09:45:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-07T14:15:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-07T18:00:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-08T08:30:00Z", sale=240)
    SaleFactory(store=bourke, timestamp="2025-01-08T11:00:00Z", sale=170)
    SaleFactory(store=bourke, timestamp="2025-01-08T14:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-09T10:45:00Z", sale=160)
    SaleFactory(store=bourke, timestamp="2025-01-09T13:30:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-09T18:45:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-10T09:30:00Z", sale=150)
    SaleFactory(store=bourke, timestamp="2025-01-10T13:00:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-10T16:15:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-11T10:00:00Z", sale=175)
    SaleFactory(store=bourke, timestamp="2025-01-11T14:00:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-11T19:30:00Z", sale=250)
    SaleFactory(store=bourke, timestamp="2025-01-12T08:15:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-12T12:30:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-12T15:45:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-13T09:00:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-13T13:15:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-13T16:30:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-14T10:30:00Z", sale=160)
    SaleFactory(store=bourke, timestamp="2025-01-14T14:45:00Z", sale=175)
    SaleFactory(store=bourke, timestamp="2025-01-14T18:00:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-15T08:00:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-15T12:00:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-15T15:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-16T09:45:00Z", sale=170)
    SaleFactory(store=bourke, timestamp="2025-01-16T13:15:00Z", sale=160)
    SaleFactory(store=bourke, timestamp="2025-01-16T18:00:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-17T08:30:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-17T12:45:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-17T17:00:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-18T09:00:00Z", sale=240)
    SaleFactory(store=bourke, timestamp="2025-01-18T13:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-18T18:15:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-19T10:00:00Z", sale=150)
    SaleFactory(store=bourke, timestamp="2025-01-19T13:45:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-19T17:30:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-20T08:15:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-20T12:00:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-20T16:30:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-21T09:30:00Z", sale=170)
    SaleFactory(store=bourke, timestamp="2025-01-21T14:15:00Z", sale=185)
    SaleFactory(store=bourke, timestamp="2025-01-21T18:00:00Z", sale=250)
    SaleFactory(store=bourke, timestamp="2025-01-22T10:00:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-22T14:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-22T17:45:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-23T09:00:00Z", sale=150)
    SaleFactory(store=bourke, timestamp="2025-01-23T12:15:00Z", sale=170)
    SaleFactory(store=bourke, timestamp="2025-01-23T16:00:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-24T08:30:00Z", sale=240)
    SaleFactory(store=bourke, timestamp="2025-01-24T11:45:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-24T15:30:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-25T09:00:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-25T13:15:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-25T18:00:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-26T10:30:00Z", sale=190)
    SaleFactory(store=bourke, timestamp="2025-01-26T14:00:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-26T17:30:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-27T09:45:00Z", sale=160)
    SaleFactory(store=bourke, timestamp="2025-01-27T13:30:00Z", sale=175)
    SaleFactory(store=bourke, timestamp="2025-01-27T16:00:00Z", sale=250)
    SaleFactory(store=bourke, timestamp="2025-01-28T08:15:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-28T12:00:00Z", sale=200)
    SaleFactory(store=bourke, timestamp="2025-01-28T17:30:00Z", sale=210)
    SaleFactory(store=bourke, timestamp="2025-01-29T10:00:00Z", sale=160)
    SaleFactory(store=bourke, timestamp="2025-01-29T14:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-29T18:15:00Z", sale=250)
    SaleFactory(store=bourke, timestamp="2025-01-30T09:30:00Z", sale=170)
    SaleFactory(store=bourke, timestamp="2025-01-30T13:00:00Z", sale=180)
    SaleFactory(store=bourke, timestamp="2025-01-30T16:45:00Z", sale=230)
    SaleFactory(store=bourke, timestamp="2025-01-31T08:45:00Z", sale=240)
    SaleFactory(store=bourke, timestamp="2025-01-31T12:30:00Z", sale=220)
    SaleFactory(store=bourke, timestamp="2025-01-31T15:30:00Z", sale=210)

    collins = StoreFactory(address="Collins St", location=melb)

    SaleFactory(store=collins, timestamp="2025-01-01T08:00:00Z", sale=120)
    SaleFactory(store=collins, timestamp="2025-01-01T12:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-01T15:00:00Z", sale=150)
    SaleFactory(store=collins, timestamp="2025-01-02T09:30:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-02T13:30:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-02T17:30:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-03T08:45:00Z", sale=170)
    SaleFactory(store=collins, timestamp="2025-01-03T12:45:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-03T16:30:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-04T10:00:00Z", sale=130)
    SaleFactory(store=collins, timestamp="2025-01-04T14:15:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-04T18:30:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-05T09:00:00Z", sale=190)
    SaleFactory(store=collins, timestamp="2025-01-05T13:15:00Z", sale=150)
    SaleFactory(store=collins, timestamp="2025-01-05T17:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-06T09:30:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-06T13:00:00Z", sale=170)
    SaleFactory(store=collins, timestamp="2025-01-06T16:30:00Z", sale=190)
    SaleFactory(store=collins, timestamp="2025-01-07T08:15:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-07T12:30:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-07T16:45:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-08T09:00:00Z", sale=250)
    SaleFactory(store=collins, timestamp="2025-01-08T12:15:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-08T16:00:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-09T09:45:00Z", sale=160)
    SaleFactory(store=collins, timestamp="2025-01-09T13:00:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-09T17:15:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-10T08:30:00Z", sale=150)
    SaleFactory(store=collins, timestamp="2025-01-10T12:30:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-10T16:00:00Z", sale=190)
    SaleFactory(store=collins, timestamp="2025-01-11T09:30:00Z", sale=170)
    SaleFactory(store=collins, timestamp="2025-01-11T13:15:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-11T17:30:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-12T08:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-12T12:45:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-12T16:00:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-13T09:15:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-13T13:30:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-13T17:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-14T08:30:00Z", sale=170)
    SaleFactory(store=collins, timestamp="2025-01-14T13:00:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-14T16:45:00Z", sale=250)
    SaleFactory(store=collins, timestamp="2025-01-15T09:00:00Z", sale=190)
    SaleFactory(store=collins, timestamp="2025-01-15T12:30:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-15T16:15:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-16T08:45:00Z", sale=160)
    SaleFactory(store=collins, timestamp="2025-01-16T13:30:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-16T17:45:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-17T09:00:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-17T12:45:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-17T17:15:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-18T09:15:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-18T13:30:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-18T17:00:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-19T08:30:00Z", sale=250)
    SaleFactory(store=collins, timestamp="2025-01-19T13:15:00Z", sale=170)
    SaleFactory(store=collins, timestamp="2025-01-19T17:30:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-20T09:00:00Z", sale=190)
    SaleFactory(store=collins, timestamp="2025-01-20T13:30:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-20T17:00:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-21T09:45:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-21T13:00:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-21T16:30:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-22T08:00:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-22T12:15:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-22T16:30:00Z", sale=250)
    SaleFactory(store=collins, timestamp="2025-01-23T09:00:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-23T12:30:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-23T16:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-24T09:30:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-24T13:00:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-24T16:45:00Z", sale=190)
    SaleFactory(store=collins, timestamp="2025-01-25T08:15:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-25T12:30:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-25T17:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-26T09:00:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-26T13:30:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-26T17:15:00Z", sale=250)
    SaleFactory(store=collins, timestamp="2025-01-27T09:30:00Z", sale=160)
    SaleFactory(store=collins, timestamp="2025-01-27T13:00:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-27T16:45:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-28T08:45:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-28T12:30:00Z", sale=210)
    SaleFactory(store=collins, timestamp="2025-01-28T16:00:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-29T09:00:00Z", sale=170)
    SaleFactory(store=collins, timestamp="2025-01-29T13:15:00Z", sale=220)
    SaleFactory(store=collins, timestamp="2025-01-29T16:30:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-30T09:00:00Z", sale=200)
    SaleFactory(store=collins, timestamp="2025-01-30T13:30:00Z", sale=180)
    SaleFactory(store=collins, timestamp="2025-01-30T16:45:00Z", sale=240)
    SaleFactory(store=collins, timestamp="2025-01-31T08:00:00Z", sale=250)
    SaleFactory(store=collins, timestamp="2025-01-31T12:00:00Z", sale=230)
    SaleFactory(store=collins, timestamp="2025-01-31T15:30:00Z", sale=210)

    sydney = LocationFactory(name="Sydney")
    george = StoreFactory(address="George St", location=sydney)

    SaleFactory(store=george, timestamp="2025-01-01T08:00:00Z", sale=135)
    SaleFactory(store=george, timestamp="2025-01-01T12:00:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-01T15:00:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-02T09:30:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-02T13:30:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-02T17:30:00Z", sale=170)
    SaleFactory(store=george, timestamp="2025-01-03T08:45:00Z", sale=160)
    SaleFactory(store=george, timestamp="2025-01-03T12:45:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-03T16:30:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-04T10:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-04T14:15:00Z", sale=185)
    SaleFactory(store=george, timestamp="2025-01-04T18:30:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-05T09:00:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-05T13:15:00Z", sale=150)
    SaleFactory(store=george, timestamp="2025-01-05T17:00:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-06T09:30:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-06T13:00:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-06T16:30:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-07T08:15:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-07T12:30:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-07T16:45:00Z", sale=185)
    SaleFactory(store=george, timestamp="2025-01-08T09:00:00Z", sale=170)
    SaleFactory(store=george, timestamp="2025-01-08T12:15:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-08T16:00:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-09T09:45:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-09T13:00:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-09T17:15:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-10T08:30:00Z", sale=160)
    SaleFactory(store=george, timestamp="2025-01-10T12:30:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-10T16:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-11T09:30:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-11T13:15:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-11T17:30:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-12T08:00:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-12T12:45:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-12T16:00:00Z", sale=170)
    SaleFactory(store=george, timestamp="2025-01-13T09:15:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-13T13:30:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-13T17:00:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-14T08:30:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-14T13:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-14T16:45:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-15T09:00:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-15T12:30:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-15T16:15:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-16T08:45:00Z", sale=150)
    SaleFactory(store=george, timestamp="2025-01-16T13:30:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-16T17:45:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-17T09:00:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-17T12:45:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-17T17:15:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-18T09:15:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-18T13:30:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-18T17:00:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-19T08:30:00Z", sale=170)
    SaleFactory(store=george, timestamp="2025-01-19T13:15:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-19T17:30:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-20T09:00:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-20T13:30:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-20T17:00:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-21T09:45:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-21T13:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-21T16:30:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-22T08:00:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-22T12:15:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-22T16:30:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-23T09:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-23T12:30:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-23T16:00:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-24T09:30:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-24T13:00:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-24T16:45:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-25T08:15:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-25T12:30:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-25T17:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-26T09:00:00Z", sale=170)
    SaleFactory(store=george, timestamp="2025-01-26T13:30:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-26T17:15:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-27T09:30:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-27T13:00:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-27T16:45:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-28T08:45:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-28T12:30:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-28T16:00:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-29T09:00:00Z", sale=220)
    SaleFactory(store=george, timestamp="2025-01-29T13:15:00Z", sale=180)
    SaleFactory(store=george, timestamp="2025-01-29T16:30:00Z", sale=250)
    SaleFactory(store=george, timestamp="2025-01-30T09:00:00Z", sale=230)
    SaleFactory(store=george, timestamp="2025-01-30T13:30:00Z", sale=210)
    SaleFactory(store=george, timestamp="2025-01-30T16:45:00Z", sale=190)
    SaleFactory(store=george, timestamp="2025-01-31T08:00:00Z", sale=200)
    SaleFactory(store=george, timestamp="2025-01-31T12:00:00Z", sale=240)
    SaleFactory(store=george, timestamp="2025-01-31T15:30:00Z", sale=220)

    StoreFactory(address="Oxford St", location=sydney)


def test_sales_report(setup_sales):
    pass
