import json


def is_json(json_data):
    print(type(json_data))
    try:
        json.loads(json_data)
        is_valid = True
        return is_valid
    except TypeError:
        is_valid = False
        return is_valid



