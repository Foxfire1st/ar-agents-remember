# mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Reopens exact typed stored terminal objects and original publication evidence, and constructs a terminal selection retaining canonical publication bytes and their SHA-256. Complete-graph validation, recovery history and journal CAS were removed from this module.

## Code Commentary

### Logic

`load_typed` reopens a named store reference and refuses a wrong object type. `load_selected_terminal` parses retained publication bytes, uses the original reused frozen run when supplied, verifies terminal/result evidence, recompiles the exact planned gate result, validates certificate publication authority and forbids a certificate on a non-green result.

`terminal_selection` retains the original result/certificate references and canonical sorted compact publication JSON with its SHA-256. It constructs a selection object but does not write an operation journal.

### Conventions

References and retained bytes name originals; no latest-pointer search or provenance reconstruction substitutes for them.

### Invariants And Boundaries

- Wrong typed objects, mismatching recompiled results and invalid original publication/evidence refuse.
- A selected certificate must still name a green result.
- Complete predecessor-graph traversal, pruning protection, input-change recovery and red-retry/terminal-replacement journal transitions are not implemented here.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References


- Terminal loading reopens original publication bytes and validates full result/certificate authority. [5]


### Cross-Repo References

No cross-repository implementation or external protocol is owned here.


No separately configured cross-repository source is used for this card.

- Exact named store objects are reopened with a required runtime type; the loaded complete-graph DTO was removed. [1]
