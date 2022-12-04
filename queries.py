import re
from typing import List, Any


def filter_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda l: param in l, data))


def filter_not_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda l: param not in l, data))


def filter_or_query(param: str, data: List[str]) -> List[str]:
    return list(filter((lambda l: any(a in l for a in param.split(' '))), data))


def filter_and_query(param: str, data: List[str]) -> List[str]:
    return list(filter((lambda l: all(a in l for a in param.split(' '))), data))


def map_query(param: str, data: List[str]) -> List[str]:
    return list(map(lambda l: ' '.join(l.split(' ')[int(a)] for a in str(param).split(' ')), data))


def unique_query(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))


def sort_query(param: str, data: List[str]) -> List[str]:
    return sorted(data, reverse=(param == 'desc'))


def limit_query(param: str, data: List[str]) -> List[str]:
    return data[:int(param)]


def regex_query(param: str, data: List[str]) -> List[str]:
    qre = re.compile(param)
    return list(filter(lambda l: qre.search(l), data))
