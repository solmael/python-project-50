#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import get_args
from gendiff.pathfinder import find_file


def main():
    args = get_args()
    diff = generate_diff(
        find_file(args.first_file), 
        find_file(args.second_file), 
        args.format
        )
    print(diff)


if __name__ == "__main__":
    main()
