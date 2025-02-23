import pytest
from gendiff import generate_diff
import os


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def read_file(file_name):
    with open(os.path.join(FIXTURES_PATH, file_name), 'r') as f:
        return f.read().strip()

@pytest.mark.parametrize("file1, file2, expected_output", [
    ('file1.json', 'file2.json', 'expected_json.txt'),
    ('file1.yml', 'file2.yml', 'expected_yaml.txt')])

def test_generate_diff(file1, file2, expected_output):
    file1_path = os.path.join(FIXTURES_PATH, file1)
    file2_path = os.path.join(FIXTURES_PATH, file2)
    expected = read_file(expected_output)
    result = generate_diff(file1_path, file2_path)
    assert result == expected
