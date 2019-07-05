import argparse

from reorder_python_imports import fix_file_contents


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if sorti would like to make changes.",
    )
    args = parser.parse_args()

    if not args.filenames:
        print("No filenames given, doing nothing.")
        return 0

    num_would_change = 0

    for filename in args.filenames:
        with open(filename, "r") as f:
            contents = f.read()
        new_contents = fix_file_contents(contents)

        if contents == new_contents:
            continue

        if args.check:
            print(f"Would reformat {filename}")
            num_would_change += 1
            continue

        print("Reordering imports in {}".format(filename))
        with open(filename, "w") as f:
            f.write(new_contents)

    if num_would_change and args.check:
        print(
            f"{num_would_change} file{'s' if num_would_change != 1 else ''} "
            f"would be reformatted"
        )
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
