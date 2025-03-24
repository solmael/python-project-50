#!/usr/bin/env python3
import os

from gendiff import generate_diff
from gendiff.cli import parsing


def main():
    args = parsing()
    possible_paths = [
        os.getcwd(),
        os.path.join(os.path.dirname(__file__), '..', '..', 
                     'tests', 'fixtures')]

    def find_file(filename):
        for path in possible_paths:
            full_path = os.path.join(path, filename)
            if os.path.isfile(full_path):
                return full_path
        raise FileNotFoundError(f"File {filename} not found")

    first_file = find_file(args.first_file)
    second_file = find_file(args.second_file)
    diff = generate_diff(first_file, second_file, format_name=args.format)
    print(diff)


if __name__ == "__main__":
    main()
