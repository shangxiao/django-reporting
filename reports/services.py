from django.db import connection, models

from .models import Order


def get_orders_by_priority():
    return Order.objects.all()


def get_order_leaderboard():
    class OrderTotals(models.Model):
        category = models.CharField(primary_key=True)
        total = models.IntegerField()

    totals = OrderTotals.objects.raw(
        """\
        select 'Total' as category, 0 as total
        """
    )

    return [{"category": o.category, "total": o.total} for o in totals]


def get_order_leaderboard_with_other():
    class OrderTotals(models.Model):
        category = models.CharField(primary_key=True)
        total = models.IntegerField()

    totals = OrderTotals.objects.raw(
        """\
        select 'Total' as category, 0 as total
        """
    )

    return [{"category": o.category, "total": o.total} for o in totals]


def get_set_from_db(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]


def series_1_to_10():
    return get_set_from_db("select 1")


def series_even_numbers_to_20():
    return get_set_from_db("select 2")


def series_date_range_jan_2025():
    return get_set_from_db("select '2025-01-01'::timestamptz")


def sales_report():
    class Sales(models.Model):
        # doesn't matter about uniqueness, just need to set a primary_key to stop Django from complaining
        date = models.DateField(primary_key=True)
        store = models.CharField()
        total = models.IntegerField()

    qs = Sales.objects.raw(
        """\
        select '2025-01-01'::date as date,
               '???' as store,
               0 as total
        """
    )

    return [
        {"date": s.date.strftime("%Y-%m-%d"), "store": s.store, "total": s.total}
        for s in qs
    ]


def sales_report_by_fortnight():
    class Sales(models.Model):
        # doesn't matter about uniqueness, just need to set a primary_key to stop Django from complaining
        date = models.DateField(primary_key=True)
        store = models.CharField()
        total = models.IntegerField()

    qs = Sales.objects.raw(
        """\
        select '2025-01-01'::date as date,
               '???' as store,
               0 as total
        """
    )

    return [
        {"date": s.date.strftime("%Y-%m-%d"), "store": s.store, "total": s.total}
        for s in qs
    ]
