# mcp/tests/test-evidence-lanes.toml

## Governing Overview

[tests route overview](overview.md)

## Purpose

The canonical evidence-lane catalog: which test modules belong to which lane, so a leaf's checks can
name the population they ran.

## Code Commentary

### Logic

The catalog assigns each current test module exactly one evidence lane. The dependency-facts
store controls and the Python load-independence scanner belong to `architecture-fitness`; the
existing knowledge reader coverage remains in `unit-regression`. Membership declares the selected
population, never that an invocation ran or passed.

### Conventions

TOML lists, one module path per row, kept sorted within the lane.

### Invariants And Boundaries

Both test catalogs stay in one canonical form; every loader refuses a duplicate or malformed entry.
A new test module that belongs to a lane is added here in the same pass.


### Registering a test module

A new test module is added to the list of its lane. `mcp/tests/test_reviewer_worklist_process.py` and
`mcp/tests/test_reviewer_worklist_reads.py` are in the `integration` list: they start real child
processes and Git repositories, and a default run with `not integration` skips them.

### Todos

No additional work is asserted by this card.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The lane catalog carries the incoming shared evidence-lane content from the L79 sync plus the lanes of the new leaf-handover and retirement-wording test modules.

## 260928-MIK-L93 — a question for the developer goes up the chain

`mcp/tests/test_developer_question_wording.py` is added to the `unit-regression` lane; no other lane changes.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The new module joins this lane. [19]
- The module the lane names. [20]

- The integration list includes the two reviewer worklist test modules. [240]

- Dependency-facts store controls belong to architecture fitness. [241]
- The bounded Python load-independence scanner belongs to architecture fitness. [242]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

## 260928-MIK-L96 The host test lanes

The lane catalog maps the new host test modules to their lane so the evidence lanes stay complete for the added cases.

- The lane catalog with the host module rows. [21]
