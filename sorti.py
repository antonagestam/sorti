import argparse
import re
from pathlib import Path
from typing import Iterable
from typing import Set

import pkg_resources
from black import find_project_root
from black import gen_python_files_in_dir
from black import Report
from reorder_python_imports import fix_file_contents

EXCLUDES = re.compile(
    r"/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist)/"
)
INCLUDES = re.compile(r"\.py$")


def get_source_files(paths: Iterable[str]) -> Iterable[Path]:
    report = Report()
    root = find_project_root((f for f in paths))
    sources: Set[Path] = set()
    for filename in paths:
        path = Path(filename)
        if path.is_dir():
            sources.update(
                gen_python_files_in_dir(
                    path=path,
                    root=root,
                    include=INCLUDES,
                    exclude=EXCLUDES,
                    report=report,
                )
            )
        elif path.is_file():
            sources.add(path)
        else:
            print(f"Error: invalid path: {path}")
            exit(1)
    return sources


def get_version() -> str:
    return pkg_resources.require("sorti")[0].version


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="*")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if sorti would like to make changes.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {get_version()}"
    )
    args = parser.parse_args()

    if not args.source:
        print("No sources given, doing nothing.")
        return 0

    sources = tuple(args.source)
    num_would_change = 0

    for path in get_source_files(sources):
        with path.open("r") as file:
            contents = file.read()
        new_contents = fix_file_contents(contents)

        if contents == new_contents:
            continue

        if args.check:
            print(f"Would reformat {path}")
            num_would_change += 1
            continue

        print(f"Reordering imports in {path}")
        with path.open("w") as file:
            file.write(new_contents)

    if num_would_change and args.check:
        print(
            f"sorti would sort imports in {num_would_change} "
            f"file{'s' if num_would_change != 1 else ''} "
        )
        return 1
    elif args.check:
        print("sorti would make no changes, all imports are sorted")
    return 0


if __name__ == "__main__":
    exit(main())
