import argparse

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

    parser.add_argument(
        "-f", "--format"
    )

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
