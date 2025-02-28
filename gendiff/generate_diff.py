from gendiff.build_diff import build_diff
from gendiff.format_diff import format_diff
from gendiff.reader import read_files


def generate_diff(file1_path, file2_path, format_name='stylish'):
    file1_data, file2_data = read_files(file1_path, file2_path)
    diff = build_diff(file1_data, file2_data)
    return format_diff(diff)
