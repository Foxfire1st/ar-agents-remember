# mcp/tests/test_untyped_sprint_rows.py

## Governing Overview

[tests overview](overview.md)

## Purpose

A sprint that commands a master without a typed row blocks neither finalize nor retire. The fixture reproduces the rows of the real sprint: a master behind a legacy seat row whose seat document names it, a master behind a seat row whose seat document names nobody, and a master with a typed row. The linkage report states the first two as facts; finalize and retire work on all three.

## Code Commentary

`_seat` builds the legacy rows and `_facts` reads the linkage report. The cases cover completing the correlated seat row, completing the master and reporting the sprint row as skipped, replacing the correlated seat row on retirement and adding a row where none stands, a retired master's kept seat document being readable while its writes refuse, a retirement row that kept a seat file never standing for a master again, a legacy commanded master called on itself, and finalize reading only the documents it needs.

## Evidence

- A retired master's kept seat document is readable, and task_doc writes that would sync its retired row deliberately refuse with the words the master is retired. [1]
- Finalize and retire work on typed rows, correlated legacy seat rows, and a commanded master with no row. [2]
