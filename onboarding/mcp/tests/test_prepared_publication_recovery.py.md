# mcp/tests/test_prepared_publication_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_prepared_publication_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09 |
| lastVerifiedCommitHash | `8133b6a9de2f787cb6c4527621a70123357aff31` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises actual Gate-5 memory preparation, private Git outputs, ledger publication, and interrupted closeout recovery. The suite uses the real prepared-memory adapter and continuation owners while retaining physical root state until final publication.

## Code Commentary

### Logic

`test_real_gate_five_prepares_then_publishes_memory_and_ledger` launches the production-shaped memory worker. `_prepare_memory_output_scenario` verifies private memory/ledger ancestry and idempotent preparation. `_interrupt_and_resume_memory_publication` injects interruptions at publication and proof boundaries, then resumes through the existing finalization owner; `_publish_and_recover_memory_outputs` verifies terminal contract and ledger state.

### Invariants And Boundaries

- Private prepared Git outputs are separate from the live roots until publication.
- Repeated preparation is idempotent and preserves the journal.
- Recovery observes proven memory before publishing the ledger and never fabricates a success after interruption.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Publication/recovery claims are backed by the retained integration suite. | `test_real_gate_five_prepares_then_publishes_memory_and_ledger` | mcp/tests/test_prepared_publication_recovery.py:22-51 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real Gate-5 memory and ledger preparation path is exercised. | `test_real_gate_five_prepares_then_publishes_memory_and_ledger`; `_prepare_memory_output_scenario` | mcp/tests/test_prepared_publication_recovery.py:22-113 |
| Publication and proof interruptions resume through the existing finalization owner. | `_interrupt_and_resume_memory_publication`; `_publish_and_recover_memory_outputs` | mcp/tests/test_prepared_publication_recovery.py:116-211 |

## Cross-Repo References

None; this suite uses local memory, ledger, and closeout owners.

## Update History

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent test sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `4a738426a4c08acfd793c6efdb499127728a2a09c841fad0bbdb089ffde90512`). No test execution or future candidate verification stamp is claimed.
