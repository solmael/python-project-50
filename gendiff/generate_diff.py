from pathlib import Path

from gendiff.build_diff import build_diff
from gendiff.format_diff import format_diff
from gendiff.parser import parse_file

SUPPORTED_FORMATS = {'.json', '.yml', '.yaml'}


def generate_diff(path_file1, path_file2,
                  format_name='stylish'):
    file1, format1 = read_file(path_file1)
    file2, format2 = read_file(path_file2)
    parced_file1 = parse_file(file1, format1)
    parced_file2 = parse_file(file2, format2)
    diff = build_diff(parced_file1, parced_file2)
    return format_diff(diff, format_name)


def read_file(path_file):
    format = Path(path_file).suffix.lower()
    if format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {format}")
    
    with open(path_file, 'r') as f:
        data = f.read()
    
    return data, format
