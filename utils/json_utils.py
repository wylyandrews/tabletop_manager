import json


def import_json(file_name):
    with open(file_name, "r") as json_file:
        return json.load(json_file)
