# mcp/tests/test_knowledge_label_operations.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**The focused behaviour of the two standalone label operations and their concurrency guard.** A label is the one
mutable field of an identity row, which is why a label edit is the only identity edit the store exposes and why it
names the row the caller read.

Each case protects one consequential outcome: the edit that writes and reads back, the stale expectation that
must not overwrite a row that moved under the caller, and the unknown identity that must not invent one.

**The standalone path needs its own evidence, and the module docstring says why**: the batch carries an
independent copy of the expectation rule in `batch_preconditions._require_identity`, so a case driven only through
the batch would stay green if the comparison in `labels.apply_*` were deleted. This module drives the standalone
entry points through the admitted destination, which is what makes that guard load-bearing — deleting the CAS in
`labels.apply_invariant_label` fails
`test_a_stale_invariant_label_expectation_refuses_and_leaves_the_row_identical`.

It is registered in `mcp/tests/test-evidence-lanes.toml` under **unit-regression** (hermetic: temporary
directories, in-process APSW databases, no integration marker).

## Code Commentary

### Logic

Six nodes, three per concept, all driven through `admitted_knowledge_destination` and the application seam's
`set_knowledge_invariant_label` / `set_knowledge_family_label`:

- `test_an_invariant_label_edit_writes_and_reads_back` and `test_a_family_label_edit_writes_and_reads_back` — the
  labelled outcome: `state="labeled"`, the row re-read carries the new label, and the returned label is the
  stored one.
- `test_a_stale_invariant_label_expectation_refuses_and_leaves_the_row_identical` and its family twin — the
  concurrency guard: a stale `expected_row_digest` returns `state="refused"` with `stale_precondition`, and the
  case re-reads the row's label **and** digest afterwards to show they are unchanged. This is the pair of nodes
  the mutation that deletes the CAS fails.
- `test_an_unknown_invariant_label_target_refuses_without_inventing_a_row` and its family twin — the unknown
  identity refuses (`unknown_invariant`/`unknown_family`) and writes nothing.

The `fixture` and `destination` fixtures build the branching knowledge fixture and an admitted destination from
it, so every case starts from records the public operations created.

### Conventions

- Cases assert on the re-read row rather than on the result alone, so a result and the store cannot both be wrong
  in the same direction unnoticed.
- The stale case names the digest it read and then proves the row did not move, which is the whole contract of a
  guarded edit.
- Registration: `mcp/tests/test-evidence-lanes.toml` `unit-regression` (row 70). Classification only, never
  execution or acceptance evidence.
- The module is also listed as a consumer of the branching fixture's registered contract
  (`knowledge-identity-branching-fixture`) — the registry derives real importers, so importing the fixture must be
  recorded there.

### Invariants And Boundaries

- **This module exists because the batch path cannot cover the guard.** Do not fold its cases into the batch
  suites: the batch's own copy of the rule would keep them green while the standalone guard was gone.
- **Both concepts get the same three cases.** The two operations share their shape in `labels.py`, and a
  divergence between them is a defect the paired cases would expose.
- **The refusal is measured, not just returned.** Each stale case re-reads the row so "the row was left
  byte-identical" is checked.
- **Boundary.** This module owns the standalone label operations' evidence. The in-batch label behaviour belongs
  to `test_candidate_batch_transaction.py` (`test_a_no_op_label_edit_inside_a_mixed_batch_is_not_reported_as_a_write`).

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's scope statement, including why the standalone path needs evidence the batch path cannot supply. [1]
- The labelled outcomes for both concepts. [2]
- The stale-expectation cases the CAS mutation fails. [3]
- The unknown-identity cases. [4]
- The fixture contract this module consumes, cited at the replacement-contract line so the anchor resolves once. [5]
- The unit-lane row that makes the module's classification explicit. [6]
- The guard and the two entry points these cases drive. [7]
- The application entry points the cases call. [8]
- The batch's independent copy of the expectation rule, which is why this module is separate. [9]

### Cross-Repo References

No cross-repository behavior is involved in this module.

No meaningful cross-repo references found.
