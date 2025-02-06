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


def data_report():
    pass
