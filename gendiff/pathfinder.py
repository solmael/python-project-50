import os

possible_paths = [
        os.getcwd(),
        os.path.join(
            os.path.dirname(__file__),
            '..', 
            'tests', 
            'fixtures')
            ]


def find_file(filename):
    for path in possible_paths:
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            return full_path
    raise FileNotFoundError(f"File {filename} not found")