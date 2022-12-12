from typing import Tuple

from flask import Flask, request, jsonify, Response

from utils import parse_request, get_data, check_requests, run_request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/perform_query', methods=['POST'])
def perform_query() -> Tuple[Response, int]:

    file_name, u_request = parse_request(request.get_json())

    if not file_name:
        return jsonify('Имя файла не указано'), 400

    if not (data := get_data(file_name)):
        return jsonify(f'Файл {file_name} не найден'), 404

    if not u_request:
        return jsonify('Ошибка запроса'), 400

    if not check_requests(u_request):
        return jsonify('Синтаксическая ошибка в запросе'), 400

    try:
        data = run_request(u_request, data)
    except:
        return jsonify('Ошибка при обработке запроса; неправильное значение'), 400

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host="localhost", port=25000, debug=True)
