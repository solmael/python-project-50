import pytest
from gendiff import generate_diff
import os


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def read_file(file_name):
    with open(os.path.join(FIXTURES_PATH, file_name), 'r') as f:
        return f.read().strip()

@pytest.mark.parametrize('file1, file2, expected_output, format_name', [
    ('file1.json', 'file2.json', 'expected.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'expected.txt', 'stylish'),
    ('file1.json', 'file2.yml', 'expected.txt', 'stylish'),
    ('file1.json', 'file2.json', 'plain_expected.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'plain_expected.txt', 'plain'),
    ('file1.json', 'file2.yml', 'plain_expected.txt', 'plain'),
    ('file1.json', 'file2.json', 'json_expected.txt', 'json'),
    ('file1.yml', 'file2.yml', 'json_expected.txt', 'json'),
    ('file1.json', 'file2.yml', 'json_expected.txt', 'json'),
    ('deep_file1.json', 'deep_file2.json', 'deep_expected.txt', 'stylish'),
    ('deep_file1.yml', 'deep_file2.yml', 'deep_expected.txt', 'stylish'),
    ('deep_file1.json', 'deep_file2.yml', 'deep_expected.txt', 'stylish'),
    ('deep_file1.json', 'deep_file2.json', 'deep_plain_expected.txt', 'plain'),
    ('deep_file1.yml', 'deep_file2.yml', 'deep_plain_expected.txt', 'plain'),
    ('deep_file1.json', 'deep_file2.yml', 'deep_plain_expected.txt', 'plain'),
    ('deep_file1.json', 'deep_file2.json', 'deep_json_expected.txt', 'json'),
    ('deep_file1.yml', 'deep_file2.yml', 'deep_json_expected.txt', 'json'),
    ('deep_file1.json', 'deep_file2.yml', 'deep_json_expected.txt', 'json')
    ])

def test_generate_diff(file1, file2, expected_output, format_name):
    file1_path = os.path.join(FIXTURES_PATH, file1)
    file2_path = os.path.join(FIXTURES_PATH, file2)
    expected = read_file(expected_output)
    result = generate_diff(file1_path, file2_path, format_name)

    assert result == expected