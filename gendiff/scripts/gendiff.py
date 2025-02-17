import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
        usage="%(prog)s [-h] first_file second_file",
        add_help=True
    )

    parser.add_argument("first_file", help="Path to the first configuration file")
    parser.add_argument("second_file", help="Path to the second configuration file")

    args = parser.parse_args()

    print(f"Comparing {args.first_file} and {args.second_file}")

if __name__ == "__main__":
    main()