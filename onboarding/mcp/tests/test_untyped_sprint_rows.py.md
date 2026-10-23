# mcp/tests/test_untyped_sprint_rows.py

## Governing Overview

[tests overview](overview.md)

## Purpose

### STOP-delta current source contract

Navigation of raw whole application results stays direct and does not reinstate a retired public reader. The later rule-14 repair changes only the skipped-row completion predicate and its comment; other row, file, linkage and retirement assertions remain unchanged.

These are current source/assertion-carrier meanings. The qualified attempt14 CODE verdict is inherited, not a Curator test run, native freeze-currentness certification or independent MEMORY acceptance. Earlier contrary accounts are historical only; unaffected contracts and typed provenance remain.

A sprint that commands a master without a typed row blocks neither finalize nor retire. The fixture reproduces the rows of the real sprint: a master behind a legacy seat row whose seat document names it, a master behind a seat row whose seat document names nobody, and a master with a typed row. The linkage report states the first two as facts; finalize and retire work on all three.

## Code Commentary

`_seat` builds the legacy rows and `_facts` reads the linkage report. The cases cover completing the correlated seat row, completing the master and reporting the sprint row as skipped, replacing the correlated seat row on retirement and adding a row where none stands, a retired master's kept seat document being readable while its writes refuse, a retirement row that kept a seat file never standing for a master again, a legacy commanded master called on itself, and finalize reading only the documents it needs.

Three MIK-R209 cases cover the census boundary: a deep sprint copy no longer refuses the master's own `task_doc` write, finalization proceeds with that copy present, and a second direct sprint document still refuses with "several commanding sprints".

The skipped-sprint-row finalization case starts its master `inProgress`, so completion is real. The
rule-14 assertion requires `Completed` and the decision array equal to its pre-finalization value: no
completion decision is appended and any preexisting entries are preserved. Already-Completed documents
remain idempotent no-write results. Both absent and ambiguous sprint-row parameters retain their dry-run,
linkage, archive-reason and unchanged sprint-source-pair assertions. These are declared source assertions,
not a fresh Curator execution.



## Evidence


- A retired master's kept seat document is readable, and task_doc writes that would sync its retired row deliberately refuse with the words the master is retired. [1]

- Finalize and retire work on typed rows, correlated legacy seat rows, and a commanded master with no row. [2]

- The skipped-row control completes an in-progress master and preserves the sprint source pair. [3]

- Navigation of raw whole application results stays direct and does not reinstate a retired public reader. The later rule-14 repair changes only the skipped-row completion predicate and its comment; other row, file, linkage and retirement assertions remain unchanged. [4]

