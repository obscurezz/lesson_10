import json


def get_from_json(jsonfile):
    with open(jsonfile, encoding='utf-8') as json_file:
        result = json.load(json_file)
        return result
