import json as make_json


def get_format_json(diff):
    return make_json.dumps(diff, indent=4)