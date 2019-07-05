# sorti

An opinionated CLI for [asottile/reorder_python_imports].

### Why?

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

I don't intend to support anything else than latest stable Python, for the
moment that is 3.7.

Any formatting issues has to be changed upstream. 

[asottile/reorder_python_imports]: https://github.com/asottile/reorder_python_imports
