from datetime import date
from unittest.mock import MagicMock

from . import coerce_date, coerce_symbols, Boxr


def get_test_client_and_session():
    session = MagicMock()
    client = Boxr('fake_app_id', session=session)
    client.base = 'http://noswayzenowayze.com/'
    return client, session


def test_coercing_a_string():
    assert coerce_date('2008-04-20') == '2008-04-20'


def test_coercing_a_date():
    assert coerce_date(date(2017, 1, 1)) == '2017-01-01'


def test_coercing_symbols_from_list():
    assert coerce_symbols(['USD', 'EUR', 'CAD']) == 'USD,EUR,CAD'


def test_get_calls_session_get():
    client, session = get_test_client_and_session()
    client.get('foobar', param1=1, param2=2)
    session.get.assert_called_with(
        'http://noswayzenowayze.com/foobar',
        params={'param1': 1, 'param2': 2, 'app_id': 'fake_app_id'}
    )


def test_getting_latest_makes_request():
    client, session = get_test_client_and_session()
    client.latest()
    assert session.get.called


def test_getting_historical_makes_request():
    client, session = get_test_client_and_session()
    client.historical('2017-04-20')
    assert session.get.called


def test_getting_currencies_makes_request():
    client, session = get_test_client_and_session()
    client.currencies()
    assert session.get.called


def test_getting_time_series_makes_request():
    client, session = get_test_client_and_session()
    client.time_series()
    assert session.get.called


def test_convert_makes_request():
    client, session = get_test_client_and_session()
    client.convert(1, 'USD', 'EUR')
    assert session.get.called


def test_getting_ohlc_makes_request():
    client, session = get_test_client_and_session()
    client.ohlc()
    assert session.get.called


def test_getting_usage_makes_request():
    client, session = get_test_client_and_session()
    client.usage()
    assert session.get.called
