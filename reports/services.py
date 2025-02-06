from django.db import connection


def get_set_from_db(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]


def series_1_to_10():
    return get_set_from_db("select generate_series(1, 10, 1)")


def series_even_numbers_to_20():
    return get_set_from_db("select generate_series(2, 20, 2)")


def series_date_range_jan_2025():
    return get_set_from_db(
        "select generate_series('2025-01-01'::timestamptz, '2025-01-31'::timestamptz, '1 day'::interval)"
    )


# demo series + all row left join onto filtered set?
# + regroup?
def sales_report():
    class Sales(models.Model):
        timestamp = models.DateTimeField()
        total = models.IntegerField()

    qs = Sales.objects.raw("""\
        select series.timestamptz
        from generate_series('2025-01-01'::timestamptz, '2025-01-31'::timestamptz, '1 day'::interval) series
        left join


    return [{
        'timestamp': s.timestamp,
        'total': s.total
    } for


# demo grouping sets
