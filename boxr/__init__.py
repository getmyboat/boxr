from requests import Session
from datetime import date


def coerce_date(d):
    '''
    Coerce whatever `d` is into a string compliant with Open Exchange Rates
    format (which is as of today yyyy-mm-dd).
    '''
    if isinstance(d, str):
        # You best be hopin you not done screwed this up
        return d
    if isinstance(d, date):
        return date.strftime(d, '%Y-%m-%d')
    return d


class Boxr:
    base = 'https://openexchangerates.org/api/'

    def __init__(self, app_id):
        self.app_id = app_id
        self.session = Session()

    def get(self, url, **kwargs):
        """
        GET from the Open Exchange Rates API.

        Function signature matches that of requests.get().
        """
        return self.session.get(
            self.base + url,
            params={**kwargs, **{'app_id': self.app_id}}
        )

    def latest(self, **kwargs):
        '''
        See https://docs.openexchangerates.org/docs/latest-json
        '''
        return self.get('latest.json', **kwargs)

    def historical(self, date, **kwargs):
        '''
        See https://docs.openexchangerates.org/docs/historical-json
        '''
        return self.get('historical/%s.json' % coerce_date(date), **kwargs)

    def currencies(self, **kwargs):
        '''
        See https://docs.openexchangerates.org/docs/currencies-json
        '''
        return self.get('currencies.json', **kwargs)

    def time_series(self, **kwargs):
        '''
        see https://docs.openexchangerates.org/docs/time-series-json
        '''
        self.get('time-series.json', **kwargs)

    def convert(self, value, frum, to, **kwargs):
        '''
        See https://docs.openexchangerates.org/docs/convert

        Note: `from` is a reserved keyword and I actually do know
        how to spell "from".
        '''
        return self.get(
            'convert/%s/%s/%s' % (value, frum, to),
            **kwargs
        )

    def ohlc(self, **kwargs):
        '''
        See https://docs.openexchangerates.org/docs/ohlc-json
        '''
        return self.get('ohlc.json', **kwargs)

    def usage(self, **kwargs):
        '''
        See https://docs.openexchangerates.org/docs/usage-json
        '''
        return self.get('usage.json', **kwargs)
