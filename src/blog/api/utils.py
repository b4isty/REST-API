import json


def is_json(data):

    try:
        json.loads(data)
        is_valid = True
        return is_valid

    except ValueError:
        is_valid = False
        return is_valid





