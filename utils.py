from collections import defaultdict
from typing import Optional, List, Tuple, Any

from constants import QUERIES


def parse_request(req: Any) -> Tuple[Optional[str], Optional[list]]:
    """
    Функция по анализу синтаксиса запроса.
    :param req: POST-запрос как есть.
    :return: возращает имя файла, отсортированный список запросов, None приводит к ошибке.
    """

    try:
        file_name: str = req.pop('file_name')
    except KeyError:
        return None, None

    d: dict = defaultdict(lambda: ['', ''])
    try:
        for key, value in req.items():
            if key[:3] == 'cmd':
                d[int(key[3:])][0] = value
            elif key[:5] == 'value':
                d[int(key[5:])][1] = value
    except:
        return file_name, None

    return file_name, [i[1] for i in sorted(d.items())]


def get_data(filename: str) -> Optional[List[str]]:
    try:
        with open('data/'+filename) as f:
            return list(map(lambda l: l.strip(), f))
    except FileNotFoundError:
        return None


def check_requests(req_list: List[str]) -> Optional[int]:
    """
    Эта функция проверяет правильность списка запросов, допустимость и парность.
    :param req_list: список запросов из функции.
    :return: возвращает 1 если все в порядке и None в противном случае
    """
    for r in req_list:
        if r[0] not in QUERIES or len(r) != 2:
            return None
    return 1


def run_request(req_list: List[str], data: List[str]) -> List[str]:
    """
    :param req_list: список запросов.
    :param data: данные.
    :return: возвращаются данные после перестановок в виде списка.
    """
    for req in req_list:
        data = QUERIES[req[0]](param=req[1], data=data)
    return data
