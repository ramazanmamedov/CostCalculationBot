import json
import config


def read_from_json():
    with open(config.JSON_DATA_PATH, "r") as read_file:
        return json.load(read_file)


def write_to_json(object):
    with open(config.JSON_DATA_PATH, "w") as write_file:
        json.dump(object, write_file)


def add_creditor(creditor):
    creditors = read_from_json()
    creditors.append(creditor)
    if(len(creditors) > 5):
        return 'Количество должников не может быть больше 5'
    for item in creditors:
        if(item['name'] == creditor['name']):
            return 'Должник с таким именем уже существует'
    write_to_json(config.JSON_DATA_PATH, creditors)
    return 'Должник успешно добавлен'


def add_credit_to_creditor(creditor_name, money):
    creditors = read_from_json()
    for item in creditors:
        if(item['name'] == creditor_name):
            item['credit'] += money
            return 'Долг успешно добавлен и теперь он составляет ' + item['credit'] + 'тг'
    return 'Должник с таким именем не найден'


def create_creditor(name):
    return {
        'name': name,
        'credit': 0
    }
