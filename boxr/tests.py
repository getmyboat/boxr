from datetime import date
from unittest.mock import patch

from . import coerce_date, Boxr


def test_coercing_a_string():
    assert coerce_date('2008-04-20') == '2008-04-20'


def test_coercing_a_date():
    assert coerce_date(date(2017, 1, 1)) == '2017-01-01'


@patch('__main__.Session')
def test_get_calls_session_get(session_mock):
    client = Boxr('fake_app_id')
    client.base = 'http://noswayzenowayze.com/'
    client.get('foobar', param1=1, param2=2)
    session_mock.return_value.get.assert_called_with(
        'http://noswayzenowayze.com/foobar',
        params={'param1': 1, 'param2': 2}
    )


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
