# mcp/tests/test_mik_r118_r124_marks.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**The focused evidence for the two record kinds (MIK-R118, MIK-R124).** One module holds the cases that
protect the weakness and dependent behaviour: the schemas and their refusals, the derived staleness and the
selective landing read, the worklist rows and which row answers each, the writer's confirmation of every
recorded value, the card line, and the master's-end refusal. It is the test file the leaf's expected-evidence
items name. The coverage is mixed: most cases build and commit real Git repositories under `tmp_path` — the
gate cases among them — while several assert over synthetic inputs (supplied selection objects and result
mappings, and monkeypatched mark rows), and the writer cases rest partly on a fixture memory pair whose
history file is written already closed. No case in the module runs a closeout operation.

## Code Commentary

### Logic

- **The record kinds.** Every weakness kind is one literal list; a weakness without a file, with an unknown
  kind or beyond the one-sentence bound is refused with its field; a closed weakness carries its task and
  commit and an open one carries none; a dependent is written with each link kind and refused without a
  link, for an untracked document, or as a second record for one document.
- **Derived state.** A file link moves when its blob differs and stands when it is the same; a record link
  moves when the stored revision differs; the derivation writes nothing into the record; a card read names
  one count per kind and never a sentence.
- **The rows.** A changed file raises the weakness row and a changed document raises its item; a standing
  weakness refuses nothing and answers its row; a `no_impact` row does not answer a changed document while
  a changed row does; a changed row cannot stand in for this task's confirmation.
- **The landing.** The answer names the documents the landing made stale and only those, a document already
  stale at the base is named and refuses nothing, an uncomputable state is named in place of the count, and
  the master's end refuses and then passes after the confirmation.
- **The writer.** Both kinds are recorded with each value read from the candidate, each refusal names its
  field, a record link names the record rather than the file it lives in, a deleted document takes its
  dependent record, and a confirming task names itself and its judgment.
- **Cost.** An ordinary landing reads only the dependents a change can move — a series master's end reads
  every document — measured at the two populations the packet names, and metadata scans are not counted as
  body reads.

### Conventions

- Real repositories are created and committed under `tmp_path`, so history, deletion and rename cases are
  exercised against Git rather than against a mock.
- The module asserts the observed behaviour; it does not restate the implementation's structure.

### Invariants And Boundaries

- **Nothing here refuses a task for a weakness.** The cases that pass an open or newly recorded weakness
  through the validator and the gate are the protection of that rule: the gate case builds a fixture leaf whose
  history file is already closed and asserts `landing_gate_refusal(request) is None` — an open weakness makes
  the gate refuse nothing for it. No case runs a closeout.
- **The card line is a count.** No case asserts a weakness sentence or a document's text on a card.

### Todos

- None.

## Evidence

- The module is the leaf's own expected evidence for both packets: 63 test functions over the schemas, the
  reads, the rows, the landing routes and the writer. That number is the module's declared test-function
  count; it is not a separately collected or executed case count, and the leaf's accepted native runs are
  evidence of their own that this module does not contain.
