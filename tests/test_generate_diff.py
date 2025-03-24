import pytest
from gendiff import generate_diff
import os


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.fixture
def expected(request):
    filename = request.param
    with open(os.path.join(FIXTURES_PATH, filename), 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize('format_name, input_files, expected', [
    # for stylish
    ('stylish', 
     ('file1.json', 
      'file2.json'), 
      'expected.txt'),
    ('stylish', 
     ('file1.yml', 
      'file2.yml'), 
      'expected.txt'),
    ('stylish', 
     ('file1.json', 
      'file2.yml'), 'expected.txt'),
    ('stylish', 
     ('deep_file1.json', 
      'deep_file2.json'), 
      'deep_expected.txt'),
    ('stylish', 
     ('deep_file1.yml', 
      'deep_file2.yml'), 
      'deep_expected.txt'),
    
    # for plain
    ('plain', 
     ('file1.json', 
      'file2.json'), 
      'plain_expected.txt'),
    ('plain', 
     ('file1.yml', 
      'file2.yml'), 
      'plain_expected.txt'),
    ('plain', 
     ('deep_file1.json', 
      'deep_file2.json'), 
      'deep_plain_expected.txt'),
    
    # for json
    ('json', 
     ('file1.json', 
      'file2.json'), 
      'json_expected.txt'),
    ('json', 
     ('deep_file1.yml', 
      'deep_file2.yml'), 
      'deep_json_expected.txt'),
    
    # mix
    ('stylish', 
     ('file1.json', 
      'file2.yml'), 
      'expected.txt'),
    ('plain', 
     ('file1.yml', 
      'file2.json'), 
      'plain_expected.txt'),
    ('json', 
     ('deep_file1.json', 
      'deep_file2.yml'), 
      'deep_json_expected.txt'),
    
    # for empty
    ('stylish', 
     ('empty1.json', 
      'empty2.yml'), 
      'empty_expected.txt'),
], indirect=['expected'])
def test_generate_diff(format_name, input_files, expected):
    file1 = os.path.join(FIXTURES_PATH, input_files[0])
    file2 = os.path.join(FIXTURES_PATH, input_files[1])
    assert generate_diff(file1, file2, format_name) == expected