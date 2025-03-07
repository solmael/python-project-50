#!/usr/bin/env python3
import argparse
import os
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
        usage="%(prog)s [-h] [-f FORMAT] first_file second_file",
        add_help=True
    )

    parser.add_argument("first_file", 
                        help="Path to the first configuration file")
    parser.add_argument("second_file", 
                        help="Path to the second configuration file")

    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')

    args = parser.parse_args()
    possible_paths = [
        os.getcwd(),
        os.path.join(os.path.dirname(__file__), '..', '..', 
                     'tests', 'fixtures')]

    def find_file(filename):
        for path in possible_paths:
            full_path = os.path.join(path, filename)
            if os.path.isfile(full_path):
                return full_path
        return None

    first_file = find_file(args.first_file)
    second_file = find_file(args.second_file)

    if not first_file:
        print(f"Error: File not found: {args.first_file}")
        return
    if not second_file:
        print(f"Error: File not found: {args.second_file}")
        return
    diff = generate_diff(first_file, second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()






@pytest.mark.parametrize("file1, file2, expected_output", [
    ('file1.json', 'file2.json', 'expected_json.txt'),
    #('file1.yaml', 'file2.yaml', 'expected_yaml.txt'),
    #('nested1.json', 'nested2.json', 'expected_nested_json.txt'),
    #('nested1.yaml', 'nested2.yaml', 'expected_nested_yaml.txt'),
])



#def test_generate_diff_file_not_found():
#    with pytest.raises(FileNotFoundError):
#        generate_diff('non_existent_file1.json', 'non_existent_file2.json')

#def test_generate_diff_invalid_file_format():
 #   file1_path = os.path.join(FIXTURES_PATH, 'invalid_format.txt')
  #  file2_path = os.path.join(FIXTURES_PATH, 'file2.json')
   # with pytest.raises(ValueError):
     #   generate_diff(file1_path, file2_path)




from gendiff.reader import read_files


def generate_diff(file1_path, file2_path):
    file1_data, file2_data = read_files(file1_path, file2_path)
    return '{\n' + generate_diff_recursive(file1_data, file2_data, 0) + '\n}'


def generate_diff_recursive(data1, data2, depth):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    indent = '  ' * depth
    diff = []

    for key in all_keys:
        if key not in data1:
            diff.append(
                f'{indent}  + {key}: '
                f'{format_value(data2[key], depth + 1)}'
            )
        elif key not in data2:
            diff.append(
                f'{indent}  - {key}: '
                f'{format_value(data1[key], depth + 1)}'
            )
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append(f'{indent}    {key}: {{')
            diff.append(generate_diff_recursive(data1[key], 
                                                data2[key], depth + 2))
            diff.append(f'{indent}    }}')
        elif data1[key] == data2[key]:
            diff.append(
                f'{indent}    {key}: '
                f'{format_value(data1[key], depth + 1)}'
            )
        else:
            diff.append(
                f'{indent}  - {key}: '
                f'{format_value(data1[key], depth + 1)}'
            )
            diff.append(
                f'{indent}  + {key}: '
                f'{format_value(data2[key], depth + 1)}'
            )

    return '\n'.join(diff)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = '  ' * depth
        lines = ['{']
        for key, val in value.items():
            lines.append(
                f'{indent}    {key}: '
                f'{format_value(val, depth + 1)}'
            )
        lines.append(f'{indent}}}')
        return '\n'.join(lines)

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    return str(value)

import pytest
from gendiff import generate_diff
import os


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def read_file(file_name):
    with open(os.path.join(FIXTURES_PATH, file_name), 'r') as f:
        return f.read().strip()

@pytest.mark.parametrize("file1, file2, expected_output", [
    ('file1.json', 'file2.json', 'expected.txt'),
    ('file1.yml', 'file2.yml', 'expected.txt'),
    ('file1.json', 'file2.yml', 'expected.txt'),
    ('deep_file1.json', 'deep_file2.json', 'deep_expected.txt'),
    ('deep_file1.yaml', 'deep_file2.yaml', 'deep_expected.txt'),
    ('deep_file1.json', 'deep_file2.yaml', 'deep_expected.txt')
    ])

def test_generate_diff(file1, file2, expected_output):
    file1_path = os.path.join(FIXTURES_PATH, file1)
    file2_path = os.path.join(FIXTURES_PATH, file2)
    expected = read_file(expected_output)
    result = generate_diff(file1_path, file2_path)
    
    expected_normalized = '\n'.join(line.strip() for line in expected.splitlines())
    result_normalized = '\n'.join(line.strip() for line in result.splitlines())
    print("\nexpected:")
    print(expected)
    print("\nactual:")
    print(result)
    assert result == expected
    #assert result_normalized == expected_normalized, f"Mismatch for {file1} and {file2}"

    if result != expected:
        # Проверим различия по строкам
    expected_lines = expected.split('\n')
    result_lines = result.split('\n')
        
    print("\nПостроковое сравнение:")
    for i, (exp_line, res_line) in enumerate(zip(expected_lines, result_lines)):
        if exp_line != res_line:
            print(f"Строка {i}:")
            print(f"Expected: '{exp_line}'")
            print(f"Actual:   '{res_line}'")
            print(f"Hex expected: {' '.join(f'{ord(c):02x}' for c in exp_line)}")
            print(f"Hex actual:   {' '.join(f'{ord(c):02x}' for c in res_line)}")
    
    assert result == expected


