# mcp/tests/test_knowledge_label_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_label_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's scope statement, including why the standalone path needs evidence the batch path cannot supply. | "the batch carries its own copy of the expectation check" | mcp/tests/test_knowledge_label_operations.py:1-10 |
| The labelled outcomes for both concepts. | "test_an_invariant_label_edit_writes_and_reads_back"; "test_a_family_label_edit_writes_and_reads_back" | mcp/tests/test_knowledge_label_operations.py:57-93; mcp/tests/test_knowledge_label_operations.py:169-204 |
| The stale-expectation cases the CAS mutation fails. | "test_a_stale_invariant_label_expectation_refuses_and_leaves_the_row_identical"; "test_a_stale_family_label_expectation_refuses_and_leaves_the_row_identical" | mcp/tests/test_knowledge_label_operations.py:94-140; mcp/tests/test_knowledge_label_operations.py:205-244 |
| The unknown-identity cases. | "test_an_unknown_invariant_label_target_refuses_without_inventing_a_row"; "test_an_unknown_family_label_target_refuses_without_inventing_a_row" | mcp/tests/test_knowledge_label_operations.py:141-168; mcp/tests/test_knowledge_label_operations.py:245-269 |
| The fixture contract this module consumes, cited at the replacement-contract line so the anchor resolves once. | "contract:knowledge-identity-branching-fixture" | mcp/tests/evidence-lifecycle.toml:1048-1048 |
| The unit-lane row that makes the module's classification explicit. | "mcp/tests/test_knowledge_label_operations.py" | mcp/tests/test-evidence-lanes.toml:70-70 |
| The guard and the two entry points these cases drive. | `apply_invariant_label`; `apply_family_label`; `set_invariant_label`; `set_family_label` | mcp/src/agents_remember/memory/knowledge/labels.py:62-99; mcp/src/agents_remember/memory/knowledge/labels.py:124-156; mcp/src/agents_remember/memory/knowledge/labels.py:40-59; mcp/src/agents_remember/memory/knowledge/labels.py:102-121 |
| The application entry points the cases call. | `set_knowledge_invariant_label`; `set_knowledge_family_label` | mcp/src/agents_remember/application/knowledge.py:224-250 |
| The batch's independent copy of the expectation rule, which is why this module is separate. | `_require_identity` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:311-348 |

## Cross-Repo References

No cross-repository behavior is involved in this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the label-operations suite (six nodes, unit-regression lane). It records the three cases per concept, the reason the module exists as a separate suite (the batch path carries an independent copy of the expectation rule and would stay green with the standalone CAS deleted), and its registration as a consumer of the branching fixture's contract. Verification metadata remains empty until closeout stamps the code commit.
