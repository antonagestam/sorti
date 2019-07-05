# sorti

An opinionated CLI for [asottile/reorder_python_imports].

## Installation

```bash
pip install reorder-python-imports
```

## Why?

This package makes the features of reorder_python_imports fit into my workflow.
I think the original project is awesome, but the CLI does not work the way I
would like it to.

My opinions diverge from asottile's on these two issues.

- https://github.com/asottile/reorder_python_imports/issues/45
- https://github.com/asottile/reorder_python_imports/issues/74 

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
