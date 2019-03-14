import pytz
from datetime import datetime


class Log:

    @classmethod
    def parse_str(cls, x):
        """
        Returns the string delimited by two characters.

        Example:
            `>>> parse_str('[my string]')`
            `'my string'`
        """
        return x[1:-1]

    @classmethod
    def parse_datetime(cls, x):
        '''
        Parses datetime with timezone formatted as:
            `[day/month/year:hour:minute:second zone]`

        Example:
            `>>> parse_datetime('13/Nov/2015:11:45:42 +0000')`
            `datetime.datetime(2015, 11, 3, 11, 45, 4, tzinfo=<UTC>)`

        Due to problems parsing the timezone (`%z`) with `datetime.strptime`, the
        timezone will be obtained using the `pytz` library.
        '''
        today = datetime.today()
        dt = datetime.strptime(f'{today.year}:{today.month}:{x[1:-1]}', '%Y:%m:%d:%H:%M:%S')
        x += ' +0000'
        dt_tz = int(x[-6:-3])*60+int(x[-3:-1])
        return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))

    @classmethod
    def read_params(cls):
        return dict(
            sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
            engine='python',
            na_values='-',
            header=None,
            usecols=range(len(Log.columns())),
            names=Log.columns(),
            converters={'time': Log.parse_datetime,
                        'request': Log.parse_str,
                        'status': str,
                        'size': str,
                        'host': str})

    @classmethod
    def columns(cls):
        return ['host', 'time', 'request', 'status', 'size']