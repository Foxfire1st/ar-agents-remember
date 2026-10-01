# test_terminal_catalog.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks terminal catalog durability: landed state stays landed, dispatch-brief receipts are idempotent and reject replacement, torn extra data refuses without erasure, concurrent upserts preserve rows, and cross-instance termination cannot be resurrected. Temporary catalog instances exercise durable state rather than a pure in-memory substitute.

The retained population also pins the catalog unit-of-work contract at the `_write_disk` boundary: a clean batch performs zero physical replacements, one or many logical mutations perform exactly one, a body exception flushes the dirty partial once and leaves later rows untouched, and `list_committed()` reads the last committed file while ordinary `get()` still sees the active batch buffer.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. The four unit-regression cases
added for the batch/contention contract patch `catalog._write_disk` and count calls, so the
assertion is about physical file replacement rather than about in-memory state: the clean case
re-upserts an equal row inside a batch and records zero writes; the dirty case mutates two rows and
records one; the dirty-partial case raises from the batch body after the first row's mutation,
records one write, asserts the first row advanced, asserts the later row did not, and then proves a
later batch can still commit one write. The committed-buffer case proves the two read surfaces are
distinct: inside a batch `get()` returns the working buffer while `list_committed()` returns the
previously committed row. Earlier coverage claims in history describe prior populations and must
not be used to recreate removed tests or claim they still run.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.
`unittest.mock.patch.object` wraps the real `_write_disk`, so the assertion counts real atomic
replacements instead of substituting a fake writer.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Keep the write-count assertions bound to `_write_disk`; do not re-express them as
`_read`/`_write` buffer assertions, which would stop proving the physical-replacement contract.
The equal-row no-op guard covers exactly one matching id; duplicate-id cleanup stays on the
replace-and-append path. Coverage percentages are diagnostic and production CRAP 20 prompts review;
neither implies an obligation to restore removed cases. Full suites and whole-candidate review
remain master-end work. This source inspection does not claim a newly executed test or acceptance
result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Landed state round trips and is not reanimated [1]
- Dispatch brief receipts are idempotent and refuse a second receipt [2]
- Read refuses torn extra data without erasing evidence [3]
- Concurrent upserts do not lose or corrupt rows [4]
- Cross instance termination is sticky and never resurrected [5]
- A batch whose rows do not change performs zero physical file replacements [6]
- Inside a batch, `get()` sees the working buffer while `list_committed()` sees the committed row [7]
- Two logical mutations in one batch produce exactly one replacement [8]
- A dirty partial flush persists earlier progress once, leaves later rows untouched, and permits a later batch [9]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
