import json as make_json


def format_json(diff):
    return make_json.dumps(diff, indent=4)