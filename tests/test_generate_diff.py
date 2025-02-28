import pytest
from gendiff import generate_diff
import os


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def read_file(file_name):
    with open(os.path.join(FIXTURES_PATH, file_name), 'r') as f:
        return f.read().strip()

@pytest.mark.parametrize('file1, file2, expected_output', [
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
    
    #expected_normalized = '\n'.join(line.strip() for line in expected.splitlines())
    #result_normalized = '\n'.join(line.strip() for line in result.splitlines())
    print('\nexpected:')
    print(expected)
    print('\nactual:')
    print(result)
    assert result == expected
    #assert result_normalized == expected_normalized, f'Mismatch for {file1} and {file2}'