from typing import Callable, Dict

import queries as queries

QUERIES: Dict[str, Callable] = {
    'filter': queries.filter_query,
    'map': queries.map_query,
    'unique': queries.unique_query,
    'sort': queries.sort_query,
    'limit': queries.limit_query,

    'filter_not': queries.filter_not_query,
    'filter_and': queries.filter_and_query,
    'filter_or': queries.filter_or_query,

    'regex': queries.regex_query,
}