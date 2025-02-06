import pytest

from .models import Order
from .services import (
    get_order_leaderboard,
    get_order_leaderboard_with_other,
    get_orders_by_priority,
)

pytestmark = pytest.mark.django_db


def test_order_report():
    """
    The client has asked for a report showing all the outstanding orders orders ordered by importance
    so the user can action the orders requiring attention.

    The priority of order status is:
     - IN_PROGRESS
     - PAID
     - SHIPPED
     - DELIVERED

    Produce a queryset that will order the following orders in this way:
    """
    Order.objects.bulk_create(
        [
            Order(product="UltraComfort Memory Foam Mattress", status="DELIVERED"),
            Order(product="ProSeries Wireless Earbuds", status="IN_PROGRESS"),
            Order(product="Sleek Stainless Steel Coffee Maker", status="SHIPPED"),
            Order(product="Eco-Friendly Bamboo Toothbrush Set", status="DELIVERED"),
            Order(product="Smart LED Desk Lamp with USB Charging", status="PAID"),
            Order(product="Luxury Cotton Bath Towel Set", status="PAID"),
            Order(product="Heavy-Duty Cordless Power Drill", status="IN_PROGRESS"),
            Order(product="Premium Leather Crossbody Bag", status="SHIPPED"),
            Order(product="Bluetooth Fitness Tracker Watch", status="DELIVERED"),
            Order(product="Foldable Portable Laptop Stand", status="DELIVERED"),
        ]
    )

    orders = get_orders_by_priority()

    assert list(orders.values("product", "status")) == [
        {"product": "Heavy-Duty Cordless Power Drill", "status": "IN_PROGRESS"},
        {"product": "ProSeries Wireless Earbuds", "status": "IN_PROGRESS"},
        {"product": "Smart LED Desk Lamp with USB Charging", "status": "PAID"},
        {"product": "Luxury Cotton Bath Towel Set", "status": "PAID"},
        {"product": "Premium Leather Crossbody Bag", "status": "SHIPPED"},
        {"product": "Sleek Stainless Steel Coffee Maker", "status": "SHIPPED"},
        {"product": "Foldable Portable Laptop Stand", "status": "DELIVERED"},
        {"product": "Eco-Friendly Bamboo Toothbrush Set", "status": "DELIVERED"},
        {"product": "Bluetooth Fitness Tracker Watch", "status": "DELIVERED"},
        {"product": "UltraComfort Memory Foam Mattress", "status": "DELIVERED"},
    ]


@pytest.fixture
def mega_sales():
    fixture = [
        ("UltraComfort Memory Foam Mattress", 18),
        ("ProSeries Wireless Earbuds", 15),
        ("Sleek Stainless Steel Coffee Maker", 20),
        ("Eco-Friendly Bamboo Toothbrush Set", 13),
        ("Smart LED Desk Lamp with USB Charging", 9),
        ("Luxury Cotton Bath Towel Set", 5),
        ("Heavy-Duty Cordless Power Drill", 15),
        ("Premium Leather Crossbody Bag", 16),
        ("Bluetooth Fitness Tracker Watch", 25),
        ("Foldable Portable Laptop Stand", 2),
    ]
    Order.objects.bulk_create(
        Order(product=product, status="DELIVERED")
        for product, quantity in fixture
        for _ in range(quantity)
    )


def test_order_leaderboard(mega_sales):
    """
    The client would like a leaderboard of the top 5 products sold, with the
    grand total at the top.

    Using a single SQL query, produce this leaderboard!

    The format should be something like:

        Total Sales: xxx
        Product 1: xxx
        ...
        Product 5: xxx

    """
    leaderboard = get_order_leaderboard()

    assert leaderboard == [
        {
            "category": "Total",
            "total": 138,
        },
        {
            "category": "Bluetooth Fitness Tracker Watch",
            "total": 25,
        },
        {
            "category": "Sleek Stainless Steel Coffee Maker",
            "total": 20,
        },
        {
            "category": "UltraComfort Memory Foam Mattress",
            "total": 18,
        },
        {
            "category": "Premium Leather Crossbody Bag",
            "total": 16,
        },
        {
            "category": "ProSeries Wireless Earbuds",
            "total": 15,
        },
    ]


def test_order_leaderboard_with_other(mega_sales):
    """
    The client was impressed with your leaderboard and has placed a wager that
    you can also just as easily add an "Other section" in the same query.

    The format should now updated as the following:

        Total Sales: xxx
        Product 1: xxx
        ...
        Product 5: xxx
        Other: xxx
    """
    leaderboard = get_order_leaderboard_with_other()

    assert leaderboard == [
        {
            "category": "Total",
            "total": 138,
        },
        {
            "category": "Bluetooth Fitness Tracker Watch",
            "total": 25,
        },
        {
            "category": "Sleek Stainless Steel Coffee Maker",
            "total": 20,
        },
        {
            "category": "UltraComfort Memory Foam Mattress",
            "total": 18,
        },
        {
            "category": "Premium Leather Crossbody Bag",
            "total": 16,
        },
        {
            "category": "ProSeries Wireless Earbuds",
            "total": 15,
        },
        {
            "category": "Other",
            "total": 44,
        },
    ]
