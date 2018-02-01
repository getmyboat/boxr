from datetime import date

from . import coerce_date


def test_coercing_a_string():
    assert coerce_date('2008-04-20') == '2008-04-20'


def test_coercing_a_date():
    assert coerce_date(date(2017, 1, 1)) == '2017-01-01'
