from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client["mydatabase"]
keyvalue = db['series']


@app.route('/', methods=['GET', 'POST', 'PUT'])
def handle_request():
    if request.method == 'GET':
        key = request.args.get('key')
        if key:
            value = db.keyvalue.find_one({'key': key})
            if value:
                return value['value']
            else:
                return 'Ключ не найден'
        else:
            return 'Ключевой параметр не указан'
    elif request.method == 'POST':
        key = request.args.get('key')
        value = request.args.get('value')
        if key and value:
            db.keyvalue.insert_one({'key': key, 'value': value})
            return 'Пара "ключ-значение" успешно создана'
        else:
            return 'Параметр ключа или значения не указан.'
    elif request.method == 'PUT':
        key = request.args.get('key')
        value = request.args.get('value')
        if key and value:
            result = db.keyvalue.update_one({'key': key}, {'$set': {'value': value}})
            if result.matched_count > 0:
                return 'Пара "ключ-значение" успешно обновлена'
            else:
                return 'Ключ не найден'
        else:
            return 'Параметр ключа и/или значения не указан'
    else:
        return 'Неподдерживаемый метод HTTP'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)