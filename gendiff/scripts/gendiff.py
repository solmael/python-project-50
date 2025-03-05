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

    first_file = find_file(args.first_file)
    second_file = find_file(args.second_file)
    diff = generate_diff(first_file, second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
