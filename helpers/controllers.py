import pandas as pd

from settings.base import LOGS_LOCATION
from models.log import Log


def find_by(attr_type, attr_val, limit=0):
    """ (str, str, int) => DataFrame
    
    Find log records by type

    >>> logs = pd.read_csv('data/access.log', **Log.read_params())
    >>> logs.empty
    False
    >>> find_by('status', '200').to_dict(orient='records') #doctest: +ELLIPSIS
    [{...}]
    >>> find_by('status', '400').to_dict(orient='records') #doctest: +ELLIPSIS
    []
    """
    logs = pd.read_csv(LOGS_LOCATION, **Log.read_params())[::-1]
    logs['path'] = logs['request'].apply(lambda val: val.split(' ')[1])
    if limit:
        return logs[logs[attr_type] == attr_val][:limit]
    return logs[logs[attr_type] == attr_val]


def get_groups(attr_col, attr_type, attr_val):
    """ (str, str, str) => dict
    
    Find log rquests by type

    >>> logs = find_by('host', 'wpbfl2-45.gate.net')
    >>> logs.empty
    False
    >>> get_groups('path', 'host', 'wpbfl2-45.gate.net') #doctest: +ELLIPSIS
    {...}
    """
    logs = find_by(attr_type, attr_val)
    return logs[['host', attr_col]].groupby('host')[attr_col].apply(list).to_dict()


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL & (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.REPORT_NDIFF),
                    verbose=True)