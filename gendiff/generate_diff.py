import os

from gendiff.build_diff import build_diff
from gendiff.formaters import format_diff
from gendiff.parser import parse_file


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def get_file_data(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return parse_file(file_content, get_extension(file_path))


def generate_diff(file1_path, file2_path, format_name='stylish'):
    data1 = get_file_data(file1_path)
    data2 = get_file_data(file2_path)
    diff_tree = build_diff(data1, data2)
    formatted_diff = format_diff(diff_tree, format_name)
    return formatted_diff


