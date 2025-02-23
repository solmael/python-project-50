import json

import yaml


def parse_file(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(file)


def read_files(file1_path, file2_path):
    file1_data = parse_file(file1_path)
    file2_data = parse_file(file2_path)
    return file1_data, file2_data