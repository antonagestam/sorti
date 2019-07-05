# sorti

An opinionated CLI for [asottile/reorder_python_imports].

## Installation

```bash
pip install sorti
```

## Usage

```bash
sorti [-h] [--check] [--version] [source [source ...]]
```

### Examples

Sorting imports in a single file

```bash
sorti my/file.py
```

Checking if any files in a directory need sorting

```bash
sorti --check my/directory
```

## Why?

This package makes the features of reorder_python_imports fit into my workflow.
I think the original project is awesome, but the CLI does not work the way I
would like it to.

My opinions diverge from asottile's on these issues.

- https://github.com/asottile/reorder_python_imports/issues/45
- https://github.com/asottile/reorder_python_imports/issues/74
- https://github.com/asottile/reorder_python_imports/pull/76

So, `sorti` will support a much narrower use case than the original project. 
The command has one flag: `--check`, which will make the command output the
files it would change and return an exit code of 1 if there are changes to be
made.

`sorti` uses source file discovery from [python/black] and aims to find the same
files, given the same inputs.

I don't intend to support anything else than latest stable Python, for the
moment that is 3.7.

[asottile/reorder_python_imports]: https://github.com/asottile/reorder_python_imports
[python/black]: https://github.com/python/black
