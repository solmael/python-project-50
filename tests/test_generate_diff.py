import pytest
from gendiff import generate_diff
import os


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.fixture
def expected(request):
    filename = request.param
    with open(os.path.join(FIXTURES_PATH, filename), 'r') as f:
        return f.read().strip()

#  уменьшил количество проверок. покрытие, вроде, должно остаться таким же
#  или нужно как-то иначе их записать?

@pytest.mark.parametrize('format_name, input_files, expected', [
    # stylish
    ('stylish', 
     [('file1.json', 'file2.json'),
      ('file1.yml', 'file2.yml'),
      ('file1.json', 'file2.yml')], 
     'expected.txt'),
    ('stylish', 
     [('deep_file1.json', 'deep_file2.json'),
      ('deep_file1.yml', 'deep_file2.yml')], 
     'deep_expected.txt'),

    # plain
    ('plain', 
     [('file1.json', 'file2.json'),
      ('file1.yml', 'file2.yml')], 
     'plain_expected.txt'),
    ('plain', 
     [('deep_file1.json', 'deep_file2.json'),
      ('deep_file1.yml', 'deep_file2.yml')], 
     'deep_plain_expected.txt'),

    # json
    ('json', 
     [('file1.json', 'file2.json'),
      ('file1.yml', 'file2.yml'),
      ('file1.json', 'file2.yml')], 
     'json_expected.txt'),
    ('json', 
     [('deep_file1.json', 'deep_file2.json'),
      ('deep_file1.yml', 'deep_file2.yml')], 
     'deep_json_expected.txt'),

    # empty
    ('stylish', 
     [('empty1.json', 'empty2.yml')], 
     'empty_expected.txt'),
], indirect=['expected'])
def test_generate_diff(format_name, input_files, expected):
    for file1_name, file2_name in input_files:
        file1 = os.path.join(FIXTURES_PATH, file1_name)
        file2 = os.path.join(FIXTURES_PATH, file2_name)
        assert generate_diff(file1, file2, format_name) == expected