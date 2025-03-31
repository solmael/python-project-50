import argparse


def get_args():
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

    return parser.parse_args()