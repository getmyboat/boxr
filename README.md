BOXR
=======================

BOXR is a Better Open Exchange Rate client -- at least better than I was able to find
elsewhere because I can trust that this one will be maintained. Since I'm maintaining it.


## Install

```
$ pip install boxr
```

## Usage

Boxr maps 1:1 with OXR api documented here: https://docs.openexchangerates.org/docs/.
This means https://openexchangerates.org/api/latest.json maps to `boxr.latest()`,
and https://openexchangerates.org/api/historical/:date.json maps to `boxr.historical(date)`.

In short

* Routes map to function names, e.g. `/latest.json` -> `latest()`
* Path params map to function arguments, e.g. `/historical/:date.json` -> `historical(date)`
* Query params map to keyword arguments, e.g. `/time-series.json?start=2017-01-01&end=2017-01-05` -> `time_series(start="2017-01-01", end='2017-01-05')`

Also note that all endpoints return `requests` response objects, so things like validation
of request or formatting the response can be done by interacting with the response object.

## Example usage

```py
from boxr import Boxr

boxr = Boxr(app_id='your_app_id')

# All calls return a `requests` Response object
latest = boxr.latest()

# And thus we get the json
result = latest.json()
```
