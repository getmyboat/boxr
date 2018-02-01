from datetime import date

from . import coerce_date


def test_coercing_a_string():
    assert coerce_date('2008-04-20') == '2008-04-20'


def test_coercing_a_date():
    assert coerce_date(date(2017, 1, 1)) == '2017-01-01'


def test_get_calls_session_get():
    pass


def test_getting_latest_makes_request():
    pass


def test_getting_historical_makes_request():
    pass


def test_getting_currencies_makes_request():
    pass


def test_getting_time_series_makes_request():
    pass


def test_getting_convert_makes_request():
    pass


def test_getting_ohlc_makes_request():
    pass


def test_getting_usage_makes_request():
    pass
